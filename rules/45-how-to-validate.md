# How to validate: every claim comes with the way to check it

James's rule, 2026-11-08. A claim without a way to check it is an opinion.

## In every response from Patch and in every worker report
End with a section titled **How to validate**: one line per claim made above it, each naming the command, URL, file or click the reader performs and the result they should see. Order it by value: the one check that proves the most comes first. If a claim cannot be validated by the reader, say so there instead of leaving it out.

## In every ticket
`## How to validate` sits right after `## Acceptance` and is written before the work starts, as part of planning. Acceptance says what must be true; How to validate says what a person does to confirm it (command and expected output, URL and what to look for, file and what it must contain); Evidence says what was observed when someone did it. A ticket cannot move to `review` with an empty How to validate section. The reviewer runs the section, not their own improvisation, and notes any step that did not match.

## In the Definition of Done
`core` gains the check "How to validate written before the work, and run by someone other than the author before approval". The weekly review ticket shows each item's first validation line so James can check in one click.

## Shape of a good line
`drew --home . validate` prints `0 error(s)` · open http://127.0.0.1:8765/about and read "Ticket tools count cards" in the first paragraph · `git log --oneline -1` in desk/ shows a commit newer than 0017e60 · the file tickets/ALGO-0002-*.md has one line under Comments, not two.

## Commands and screenshots (James, 2026-11-08)
James: "reminder that how to validate and associated commands and helpful screenshots should all be part of a good ticket." Every ticket carries a `## Commands` section with the exact, copy-pasteable commands for its work and its validation, and attaches the screenshots that show the before and the after (Attachments, through the ticket page); a Report that names a command without its output, or a UI change without a screenshot, is incomplete.
