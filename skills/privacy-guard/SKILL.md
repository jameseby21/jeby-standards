---
name: privacy-guard
description: "A sharper partner of rule 30 that closes the ways a private term still reaches the store: a private name seen in any input is added to the private denylist the same turn, the whole store is scanned each pass (not only the staged diff), commit messages and hand-offs from coworkers or outside AI are scanned before they are committed, and replacements are roles in brackets that keep the sentence's meaning. Use before every commit, when any intake, report or comment is written or received, at the close of every pass, and when James writes $privacy-guard. Pairs with readback."
---

# Privacy guard: the scan covers everything that is written, and the list grows the moment a name is seen

**Pairs with `readback`.** Privacy-guard decides what must be scanned and what counts as private; readback proves the scan was read back from the scanner's own output and that the fixed text really changed. Rule 30 (the privacy boundary) is the base; this skill adds the checks that were missing when private terms got through anyway. Related and not restated here: rule 80 (never print a secret value, never rewrite history without approval), rule 26 (folder audiences), `housekeeping` (where things live).

> "let's be even way more strict on this because I lack experience here but it's vital" (James, 2026-11-11, decision 104)

**Case:** on 2026-11-12 and 2026-11-13 five leaks reached the store even though a scanner existed (failure catalog C1; SEC-0019). Seven files written before the stricter rule held 21 lines with private terms: former employers, a neighborhood and a family relationship in five intake hand-offs. A partner's contact, a family member, was named in a tracked ticket comment, because the scanner did not yet know that name. A real condo street address with its unit number sat in JRE-0154 as a search example. In each case the scanner was only run on the staged diff, or did not know the term.

## What counts as private (decision 104, rule 30)

A street address with a unit number; an employer, current or former; a family relationship or a family member's name; a health word; the name of a partner's contact; a neighborhood or other narrowing place; a pronoun or role that narrows to one person; a real company linked to one of the above. These count as names. The list of exact terms lives only in the private folder (`~/.claude/jeby-private/`); this skill never prints it, pastes it, or copies it into a ticket, brief, commit or reply.

## Rules

1. **A private name seen in any input goes onto the denylist the same turn.** Any input counts: the owner's message, a coworker's entry, an outside AI package, a worker's report, a file opened for another reason. The addition is made in the private folder only.
   **Check:** run the scanner on the file or text where the name was seen; it reports a hit there. Then add the name and run it again; the hit count is unchanged and the term is now matched by the list, not by chance. Do not paste the term into the reply. Report "term added" with the category only.
2. **The whole store is scanned each pass, not only the staged diff.** Older files were written under older rules and a new denylist entry applies to them too.
   **Check:** `git ls-files -z -- '*.md' '*.yaml' '*.json' '*.toml' '*.txt' '*.csv' '*.html' | xargs -0 <the venv python> -X utf8 -I ~/.claude/jeby-private/private_scan.py` prints `private_scan: clean` (SEC-0019). Run it in every repository the pass touched and name each in the report. A repository not scanned is marked "Not run".
3. **Commit messages are scanned as well as files.** A message is text the store keeps forever.
   **Check:** before `git commit`, write the message to a scratch file named by ticket id and run the scanner on it; after the commit, run it on `git log -1 --format=%B` saved the same way, then delete the scratch file. The commit hook (MGMT-0034) is the backstop and does not replace this check.
4. **Hand-offs are scanned before they are committed.** Coworker entries, intake folders and outside AI packages come in as files; each one is scanned where it landed, and cleaned, before it is staged (decisions 98 and 104). A hand-off is never committed first and cleaned later.
   **Check:** `git diff --cached --name-only` lists no intake file whose scan result is missing from the report; each such file has a clean scan line.
5. **Reports, ticket text and comments are text too.** Worker reports and Patch's own comments are where the partner contact's name and the employer terms appeared (failure catalog C1).
   **Check:** run the scanner over `tickets/` and the pass's report files before committing them, including text pasted from a worker (`delegation`, rule 9).
6. **Replace with a role in brackets that keeps the sentence's meaning.** "[former employer A]", "[family member]", "[a condo address, unit omitted]". A demo or example whose sample would stop working with a role is given another sample of the same kind, so the logic still runs.
   **Check:** reread the changed sentence without the original; it still says what it said. Rescan clean. Run any demo or test the sample fed and confirm it passes.
7. **A folder named after a person or a partner holds only what they may see (rule 26).** Internal material sits in "Internal - <name>"; secrets never sit in a Drive folder (SEC-0018, failure catalog D8).
   **Check:** before any share, list the folder (`ls` the path) and write, per item, who may see it. Any item the named person may not see is moved before the share, and the move is logged with old path, new path and time (`reproducibility`).
8. **Findings are reported masked.** A report gives the file, the line number and the category, never the term, and never the denylist (rule 80 item 2).
   **Check:** search the reply and the ticket text just written for any scanner entry; the scanner run on them prints clean.
9. **History is not rewritten by this skill.** A term already in older commits is reported, and the owner of security decides whether more is needed before any public edition (rule 80 item 1; SEC-0019).
   **Check:** the report says "history not rewritten" and names who decides; `git log` shows no rewritten or force-pushed commit.
10. **A public edition is scanned before its first push** (rule 30), including every file the build generates.
   **Check:** the scan over the build output folder prints clean, and the report names the folder scanned.

## Check before done

- The whole-store scan of rule 2 printed clean in every repository touched, or the report says "Not run" for the ones it did not reach.
- The new commit's message and every staged intake file were scanned (rules 3 and 4).
- Any name newly seen this turn is on the denylist and was not printed anywhere (rules 1 and 8).
- No folder was shared without the per-item audience list of rule 7.

## Applied

- 2026-11-13: SEC-0019 cleaned seven older files (21 lines) with roles in brackets, a swapped demo neighborhood and the partner contact's name added to the scanner; its How to validate runs the whole-store command above (expected clean) and the same command on the parent commit (expected hits, so the check discriminates). History was not rewritten and the question went to the owner of security (SEC-0019).
- 2026-11-13: the partner-named Drive folder was renamed "Internal - <name> (personal backup, never share)" before any share (SEC-0018, MGMT-0051).
