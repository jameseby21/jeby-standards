# Failure catalog: the most common and the worst so far

Each entry is a failure that reached James, with the rule that prevents it (QA) and the check that catches it (QC). Sources: standards/lessons/LESSONS.md, jeby-us/docs/LESSONS.md, the jRE decisions and lessons record, and the main session's records up to 2026-11-12. Newest cases are added at the bottom of their group.

## A. Claims that were not true

| # | Failure | Example | QA rule | QC check |
| --- | --- | --- | --- | --- |
| A1 | Evidence written from the plan, not the result | "both sites built" written before reading a failed exit code (JEBYUS-0001) | Evidence after the command returns, with its exit code | Re-derive one claimed result from a different source (the artifact, not the log) |
| A2 | Mock or unit test reported as runtime proof | Tests green while the running tool still failed (DESK-0082) | A mocked test is coverage, never runtime proof | Check the claim on the instance the user runs |
| A3 | Acceptance not literally met but reported done | The scan command counts per cell while the acceptance said "same count as the playground" (BSA-0091) | Each acceptance line is marked met, not met, or changed with a reason | Read each acceptance line against the evidence, line by line |
| A4 | Partial work reported as done | A pass meant to cover every workable ticket covered one area (2026-11-12) | Scope is the whole ask; any shrinking is stated first | Compare the request's own words ("any", "all", lists) with what was delivered |
| A5 | A commit message describes files the commit does not contain | A commit said it carried a privacy fix to five files, but only the ticket folders were staged; the five files stayed uncommitted until a later status check (SEC-0019, 2026-11-13) | Write the message from `git diff --cached --stat`, not from the plan | After each commit, compare `git show --stat HEAD` with the message, and run `git status --short` to see nothing the message names is left behind |

## B. Right fix, wrong place

| # | Failure | Example | QA rule | QC check |
| --- | --- | --- | --- | --- |
| B1 | Fixed in the repo, not where the user looks | Search and the declutter built 11-08 but unmerged for days (MGMT-0035) | Built but not merged or installed counts as not running | Check the installed version or the live URL, not the branch |
| B2 | Browser or process ran stale code | Approve failed on a cached pre-fix script (DESK-0257); old modules under a running server (DESK-0095) | Version every asset; never reinstall under a running instance | Load the page fresh and note the version and commit the user's instance reports |
| B3 | Link or port sent without checking | A link to a stopped preview on 8766 (LIFE-0015) | Check every link before sending it (whats-running) | Request every link in the reply and record the status code |
| B4 | Works here, fails on a clean checkout | Build failed on a clean Windows checkout (JEBYUS-0047) | A PR that says it builds shows a clean-checkout build per OS, or names the OS unverified | Build from a fresh clone, or say which OS is unverified |

## C. Privacy and the owner's voice

| # | Failure | Example | QA rule | QC check |
| --- | --- | --- | --- | --- |
| C1 | Private names in tickets or commits | Employer and family terms in worker Reports and ticket text (2026-11-12, four times) | The private scan runs before every commit, including on report text | Run the scan on everything the request committed |
| C2 | The owner's own words replaced | A voice pass rewrote James's About line and his QR title (JEBYUS-0075) | James's words win | Diff the delivered text against every line James quoted in the ticket |
| C3 | Invented facts in public copy | A worker attached an award to a club with no source | No invented facts; use [brackets] and list them | Every new factual sentence traces to a source in the repo or a ticket quote |
| C4 | Overpromising on public pages | "Every project has a free version" when most were briefs | Every listing shows its real state | For each public promise, find the thing it promises |

## D. Process and repetition

| # | Failure | Example | QA rule | QC check |
| --- | --- | --- | --- | --- |
| D1 | James had to ask twice or three times | A merge handed to James although `git` could do it (JEBYUS-0001, asked three times) | A second ask is an emergency; never hand over a step a present tool can do | Search the request for "again", "already asked", "I said" |
| D2 | How to validate missing or written after the work | 958 of 1,469 open tickets had none (DESK-0258) | Written before the work, as part of planning | Check that the section existed in the ticket's previous commit |
| D3 | Work duplicated or the same id allocated twice | Ids reserved by open store PRs were invisible (DESK-0248) | Check open PRs and running agents before allocating | Look for two tickets or two PRs with the same outcome or id |
| D4 | A user-facing feature built without design | Four screens filed without a Chaz design ticket | Anything a person sees gets a design ticket first | For each new screen, find its design ticket |
| D6 | A rule breach raised as a question | Coworker sign-offs arrived stamped "james (as lily)" through Desk's Act as menu; Patch asked James whether they counted instead of flagging Act as as a breach of decision 108 (2026-11-13, DESK-0261) | When a feature or record breaks a standing rule, report the breach and file the fix; never ask the owner whether to accept it | For each question to the owner, search DECISIONS.md and the rules for an answer he already gave |
| D7 | An ask to the owner without its meaning, his step or its ticket | "Licensing: no source is licence-cleared yet, so the public build must not ship before a licence list exists", with no meaning, no step and no ticket id (2026-11-13) | Every ask carries the five parts of gps "Asks to James" | For each ask in the reply, find the five parts |
| D8 | A folder whose name promises one audience holds another's material | The partner-named Drive folder held internal notes and a folder of secrets, while James was about to share it with the partner (SEC-0018, 2026-11-13) | A partner-named folder holds only what the partner may see; internal material sits in "Internal - <name>" (rule 26) | Before any share, list the folder's contents and confirm each item's audience |
| D5 | Windows, servers or profiles left open | Three terminals left open by previews | Windowless, recorded by PID, stopped at the end | List the processes the session started that are still running |

## E. Checks that did not check

| # | Failure | Example | QA rule | QC check |
| --- | --- | --- | --- | --- |
| E1 | A check that passes or fails by timing | Hover checks failed 2 of 3 runs (CONS-0078) | Wait for the state, never a fixed time | Run the check three times |
| E2 | A check that would pass without the change | A grep for a word that never existed | Every validation step must fail on the old version | Run one validation step against the base branch; if it passes there, it proves nothing |
| E3 | A screenshot taken and not looked at | 390 px shots captured, never read | Look at what you produced | Open one screenshot the worker cited and confirm it shows the claimed state |
| E5 | An instruction to the owner not checked against the real screen or command | Drive steps "tray icon, Settings, Add another account" (it is under the profile picture) and "/mcp, reconnect Google Drive" (typed as one command and refused) (MGMT-0044, 2026-11-13) | Check every click path against the vendor's help or a screenshot, and every command against the tool's documentation, before sending | Pick one owner step in the reply and find the help page or doc it came from |
| E4 | Numbers changed before the baseline was reproduced | (good practice) the model replica was reconciled to the dollar before any change | Reproduce the original before changing it | Re-run the reconciliation and confirm the difference rows are zero |
