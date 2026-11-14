"""Check that promoted.txt and the installed skills agree (STD-0062).

Every skill installed in ~/.claude/skills/ must be listed in skills/promoted.txt, every listed skill must be installed, and for a skill whose
source is in this repository (skills/<name>/), every file of the installed copy must match the source byte for byte.
Usage: python scripts/check_promoted.py [--skills-dir DIR]   Prints each difference and `N differences`; exit 1 when N > 0.
"""
import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORE = {"synced"}  # the claude.ai-synced skills folder is managed outside this repository


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-dir", default=str(Path.home() / ".claude" / "skills"))
    a = ap.parse_args()
    installed_dir = Path(a.skills_dir)
    promoted = [l.strip() for l in (ROOT / "skills" / "promoted.txt").read_text(encoding="utf-8").splitlines()
                if l.strip() and not l.startswith("#")]
    installed = sorted(d.name for d in installed_dir.iterdir() if d.is_dir() and d.name not in IGNORE and not d.name.startswith(".")) if installed_dir.exists() else []
    diffs = []
    diffs += [f"installed but not in promoted.txt: {n}" for n in installed if n not in promoted]
    diffs += [f"in promoted.txt but not installed: {n}" for n in promoted if n not in installed]
    for n in promoted:
        src = ROOT / "skills" / n
        if not src.is_dir() or n not in installed:
            continue
        for f in sorted(src.rglob("*")):
            if f.is_file():
                g = installed_dir / n / f.relative_to(src)
                if not g.exists():
                    diffs.append(f"missing from the installed copy: {n}/{f.relative_to(src).as_posix()}")
                elif digest(f) != digest(g):
                    diffs.append(f"installed copy differs from the source: {n}/{f.relative_to(src).as_posix()}")
    try:  # every installed SKILL.md must have frontmatter that parses, with a name and a description (the gps colon, 2026-11-13)
        import yaml
        for n in installed:
            f = installed_dir / n / "SKILL.md"
            parts = f.read_text(encoding="utf-8").split("---") if f.exists() else []
            try:
                meta = yaml.safe_load(parts[1]) if len(parts) > 2 else None
                if not (isinstance(meta, dict) and meta.get("name") and meta.get("description")):
                    diffs.append(f"frontmatter lacks a name or description: {n}")
            except yaml.YAMLError as e:
                diffs.append(f"frontmatter does not parse: {n} ({str(e).splitlines()[0]})")
    except ImportError:
        print("note: PyYAML not installed; frontmatter not checked")
    for d in diffs:
        print(d)
    print(f"{len(diffs)} differences")
    return 1 if diffs else 0


if __name__ == "__main__":
    sys.exit(main())
