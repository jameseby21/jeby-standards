---
name: readback
description: "Every write is read back from where it lives before it is reported: a commit message is written from the staged diff and checked against the commit, an edited file or field is re-read, a Desk comment is fetched from the ticket page, a screenshot is opened and described, a link is requested, a count is recomputed from the files instead of from the tool that wrote it, an instruction given to the owner is checked against the vendor's screen or docs, and a claimed completion is compared with the request's own list. Use before any sentence that says something was written, saved, committed, posted, sent, fixed or counted, and when James writes $readback. A sharpening of common-sense; pairs with privacy-guard."
---

# Readback: say it is written only after reading it where it lives

**Pairs with `privacy-guard`; sharpens `common-sense`.** Common-sense says a claim of completion must match what can be observed; readback names the observation for each kind of write, so the cheapest decisive look is never skipped. Privacy-guard's scans are readbacks too: the clean result is read from the scanner's own output, never assumed. Related and not restated here: rule 40 (claimed is not run; evidence from the exit code and output), `whats-running` (links answered, instance named), `qc` (the independent checker repeats one of these by a different route).

**Case:** a commit message described a privacy fix to five files that the commit did not stage; they sat uncommitted until the next status check (SEC-0019, 2026-11-13, failure catalog A5). A script tagged six tickets by rewriting a line they did not have, so nothing changed, while its comment said "Tagged health" (lesson of 2026-11-10, DESK-0212 prep). A comment form let one click store two identical comments (lesson of 2026-11-08). Screenshots at 390 px were captured and never opened (failure catalog E3). Drive steps given to the owner from memory were wrong twice (failure catalog E5, MGMT-0044, 2026-11-13). A pass meant to cover every workable ticket covered one area and was reported as done (failure catalog A4, 2026-11-12). In each, the write happened or was planned, and nobody read it back.

## Rules

1. **A commit message is written from the staged diff and checked against the commit.** Read `git diff --cached --stat` first and write the message from it, never from the plan (lesson of 2026-11-13). Afterwards, compare what the commit holds with what the message says.
   **Check:** `git show --stat HEAD` lists every file the message names and none it does not; `git status --short` shows nothing the message names left behind (failure catalog A5).
2. **A file or field edit is re-read after the write.** A script that edits a field adds the line when it is missing, then reads the field back and asserts the value before it writes any comment or report that claims the change (lesson of 2026-11-10).
   **Check:** `grep -n "<field>:" <file>` (or the tool's own `--help`-documented show command) prints the new value; the claim in the report quotes the printed line.
3. **A Desk comment is fetched from the ticket page.** Posting is not proof it saved, appeared once and was attributed correctly.
   **Check:** `curl -s http://127.0.0.1:8765/ticket/<ID>` (the owner's Desk; name the instance per `whats-running`) contains the comment text exactly once, or read the ticket file's Comments section: one line, not two (lesson of 2026-11-08).
4. **A screenshot is opened and described.** A captured image proves a capture, not the state it was meant to show.
   **Check:** open the image file with the image reader, and write one sentence in the report saying what it shows (for example "the timeline section lists five events, newest first"). A screenshot cited and not described is marked "Not looked at" (failure catalog E3).
5. **A link is requested before it is sent.** A link that was not requested is a guess.
   **Check:** `curl -s -o /dev/null -w "%{http_code}" <url>` prints the expected code in the same turn, and the report states the code beside the link (failure catalog B3; `whats-running` rule 1).
6. **A count is recomputed from the files, not from the tool that wrote it.** A tool that made a number can repeat its own mistake.
   **Check:** compute the number by a second route and compare: `ls tickets | wc -l`, `grep -l "^status: ready" tickets/*.md | wc -l`, `git ls-files | wc -l`, `gh pr list --state open --json number --jq length`. The two numbers match, or the report shows both and the difference (and `reproducibility` rule 8 for generated facts).
7. **An instruction given to the owner is checked against the vendor's screen or documentation.** Every click path and every command (spelled exactly as he must type it) is checked first against the vendor's help page, the tool's `--help` or a screenshot (lesson of 2026-11-13; failure catalog E5).
   **Check:** pick each owner step in the reply and write its source beside it (the help page title or the `--help` line). A step with no source is either checked now or marked "Not checked against the vendor" in red.
8. **A claimed completion is compared with the request's own list.** Copy the request's own words ("any", "all", each numbered item, each named file) into the report and mark each with its evidence or its reason for not being done (failure catalog A4; lesson of 2026-11-12). Any shortfall is stated in the reply's first lines, never discovered by the owner.
   **Check:** the number of items the request listed equals the number of items the report marks, each met, not met or changed with a reason; a total on the request with no matching total in the report is a defect.
9. **The readback is named in the report.** A report line for a write carries the command that read it back and what it printed, so the reader can run the same one (rule 40; the How to validate section of the report leads with the one that proves the most).
   **Check:** each "done", "saved", "committed", "posted" in the reply has its readback command beside it, or says "Not run".

## Check before done

- For every write in the reply (commit, edit, comment, screenshot, link, count, owner step, completion), the readback of its rule was run in this turn and its output is in the report.
- `git show --stat HEAD` agrees with the commit message; `git status --short` has nothing left behind that the message names.
- The request's list and the report's list have the same length.

## Applied

- 2026-11-13: the SEC-0019 commit that described five unstaged files was caught by `git status --short` at the next check, committed separately and recorded as failure catalog A5 and a lessons row. The check that would have caught it at the time is rule 1.
- 2026-11-13: the Drive steps given from memory (MGMT-0044, failure catalog E5) produced rule 7: each click path and command is checked against the vendor's own help or screen before it is sent.
