"""Refuse a commit that adds a private string (standards rule 30, 2026-11-11).

The denylist lives only in ~/.claude/jeby-private/denylist.txt (or $JEBY_DENYLIST), one term per line:
  term        case-insensitive substring, matched at word boundaries
  cs:Term     case-sensitive, word boundaries (for short words such as acronyms)
  # comment
Usage:
  python private_scan.py               scan lines added in the staged diff of the current repo (pre-commit)
  python private_scan.py PATH ...      scan whole files
  python private_scan.py --self-test   prove the matcher with a temporary denylist
Exit 1 on any hit; prints file:line and the matched term masked to its first letter.
"""
import os, re, subprocess, sys, tempfile
from pathlib import Path

def load(path):
    pats = []
    p = Path(path)
    if not p.exists():
        return pats
    for raw in p.read_text(encoding="utf-8").splitlines():
        t = raw.strip()
        if not t or t.startswith("#"):
            continue
        cs = t.startswith("cs:")
        term = t[3:] if cs else t
        pats.append((term, re.compile(r"(?<![\w])" + re.escape(term) + r"(?![\w])", 0 if cs else re.I)))
    return pats

def mask(term):
    return term[0] + "*" * (len(term) - 1)

def scan_lines(items, pats):
    hits = []
    for where, line in items:
        for term, rx in pats:
            if rx.search(line):
                hits.append(f"{where}: private term {mask(term)}")
    return hits

def staged_items():
    diff = subprocess.run(["git", "diff", "--cached", "-U0", "--no-color"], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    items, f, n = [], "?", 0
    for line in diff.splitlines():
        if line.startswith("+++ "):
            f = line[6:] if line.startswith("+++ b/") else line[4:]
        elif line.startswith("@@"):
            m = re.search(r"\+(\d+)", line); n = int(m.group(1)) if m else 0
        elif line.startswith("+") and not line.startswith("+++"):
            items.append((f"{f}:{n}", line[1:])); n += 1
    return items

def file_items(paths):
    for p in paths:
        for i, line in enumerate(Path(p).read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            yield (f"{p}:{i}", line)

def self_test():
    with tempfile.TemporaryDirectory() as d:
        dl = Path(d) / "deny.txt"
        dl.write_text("Acme Widgets\ncs:XQ\n# comment\n", encoding="utf-8")
        pats = load(dl)
        assert scan_lines([("a:1", "works at acme widgets now")], pats), "case-insensitive term"
        assert not scan_lines([("a:2", "acmewidgetsx")], pats), "word boundary"
        assert scan_lines([("a:3", "the XQ detail")], pats), "case-sensitive term"
        assert not scan_lines([("a:4", "the xq detail")], pats), "case-sensitive miss"
    print("private_scan self-test: 4 of 4 passed")

def main(argv):
    if argv[:1] == ["--self-test"]:
        self_test(); return 0
    path = os.environ.get("JEBY_DENYLIST", str(Path.home() / ".claude" / "jeby-private" / "denylist.txt"))
    pats = load(path)
    if not pats:
        print(f"private_scan: no denylist at {path}; nothing checked"); return 0
    hits = scan_lines(list(file_items(argv)) if argv else staged_items(), pats)
    for h in hits: print(h)
    if hits:
        print(f"private_scan: {len(hits)} hit(s); commit refused. Replace with a role or business term (rule 30)."); return 1
    print(f"private_scan: clean ({len(pats)} terms checked)"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
