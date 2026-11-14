---
name: delegation
description: "A brief is the only thing a worker has, so write it complete, bound the worker's time, and take the result into the record. Every brief states goal, exclusions, files, scope, effort, model, a time box, the privacy line, the evidence line and the exact report wanted; a time box is enforced by a wake-up check; a worker waiting on a background run has not finished; workers never stop processes by name; a workflow states its agent count and token estimate first and logs what it dropped; one agent per topic; the worker's report is pasted into the ticket. Use whenever an agent, subagent, workflow or fork is about to be started or has reported, and when James writes $delegation. Pairs with release."
---

# Delegation: a complete brief, a bounded worker, a result in the record

**Pairs with `release`.** Delegation gets the work built; release gets the built work onto the owner's screen. A delegated task is not done when the worker stops: it is done when the report is in the ticket and the change has reached where the owner looks. Related and not restated here: rule 70 (the model and effort table, the ledger, one agent per topic), `follow-through` (the main session dispatches ready work), `housekeeping` (stopping workers and processes at the end).

> "that is precisely your job to delegate" (James, 2026-11-08, after a design was delivered and no worker was started for its build)

> "There's still an agent running? But I left like 7 hours ago" (James, 2026-11-08, about a worker that nothing bounded)

## Rules

1. **Every brief states ten things:** goal in one sentence, what is already ruled out, the files worth reading, the scope (what the worker may change and nothing else), the effort, the model, a time box, the privacy line, the evidence line, and the exact report wanted (rule 70 section 3). A brief that cannot be written clearly means the task is not understood yet: stop and understand it first.
   **Check:** read the brief before sending and tick the ten items against it. A missing item is added, not assumed. The dispatch commit or ticket comment names the time box.
2. **The privacy line is in the brief.** The worker is told which terms are private as roles ("no names, employers, addresses, health words") without the list being pasted, and that its output is scanned (`privacy-guard`). The private folder's contents never go into a brief (rule 30).
   **Check:** the brief carries the line, and a search of the brief text for any entry the private scanner knows prints clean.
3. **The evidence line is in the brief.** The worker reports the exact commands, where they ran and what they printed; anything not run is marked "Not run" (rule 40).
   **Check:** the returned report has a command with its output for every claim; a claim without one is sent back, not accepted.
4. **A time box is enforced, not hoped for.** The box is twice the ticket's effort upper bound. At the start, set a wake-up for the box; at the wake-up, if the worker is still running, message it to commit what it has, mark unmet lines unmet and report (lesson of 2026-11-08, CONS-0078 worker, 3 h 40 min unwatched).
   **Check:** the ledger shows each running worker with its start time and box end; a worker past its box with no message sent is a defect in the log.
5. **A worker that ends its turn "waiting on a background suite" has not finished.** Tests, builds and checks run in the foreground with a timeout, and the worker never ends its turn while something it started is running. A run longer than the tool's limit is split into foreground parts (lesson DESK-0211: three commits unpushed, no pull request, headless browsers orphaned for half an hour).
   **Check:** read the returned result for the word "waiting", "in the background" or "will check"; if present, the work is unfinished. Then list the processes the worker recorded and confirm none is alive.
6. **Workers never match processes by name.** A process is stopped only by the PID its starter recorded; a test harness puts its own PID in its temporary profile name (lesson DESK-0171: 18 headless browsers stopped by a shared prefix that could have hit another run). The brief says so.
   **Check:** search the worker's commands for `Stop-Process -Name`, `taskkill /IM`, `pkill` and `Get-Process <name>`; any hit is a defect, and the report lists each PID stopped and who recorded it.
7. **A workflow states its size before it runs and logs what it dropped.** Before launching more than 50 agents, write the agent count and an expected token estimate in the reply, run early in the week, and use the fewest batches a deterministic checker allows (lesson DESK-0210: about 27.5 million tokens and a weekly limit reached, with seven agents in other workflows cut off mid-task). Every long agent writes its result to a file or commit as it goes. The after-action report lists what was dropped, cut or not run.
   **Check:** the reply before the launch contains the count and the estimate; after the run, the cut-off agents are listed, and `git status` plus `git log` in each worktree show nothing finished and unsaved.
8. **One agent per topic at a time.** Before starting one, check the ledger for a running agent on the same topic and wait for it or message it (rule 70 section 3; skill `housekeeping`, anti-duplication). Work that was delegated is not also run inline.
   **Check:** the ledger lists at most one running agent per topic, and the main session's own tool calls for the same period do not repeat a delegated task.
9. **The worker's report goes into the ticket, not the scratchpad.** The main session pastes it into the ticket's Report the same turn it arrives (rule 70 section 6), with the commit ids it names.
   **Check:** for each agent that reported, the ticket's Report section holds its text and `git log` holds its commits; a scratchpad file is not the only copy (`housekeeping`).
10. **A reported worker or idle worker is stopped.** Once a worker has reported or is idle, it is stopped, and the ledger says so.
   **Check:** the list of running agents is empty, or each one is named with why it stays.

## Check before done

- Each brief sent this turn has the ten items of rule 1, and the time box is on a wake-up.
- No worker result reads "waiting"; no process from the run is alive except those listed with PID and reason.
- Every report that arrived is in its ticket.
- Any workflow launched stated its count and estimate, and the after-action lists what it dropped.

## Applied

- 2026-11-13: first use is this draft's own brief (goal, exclusions, files, scope, effort, model, a 40-minute time box, the names-as-roles privacy line and the exact report wanted); whether a wake-up was set for its box is not recorded here and is marked Not run until the ledger shows it.
- Sources of the rules: lessons rows of 2026-11-08 (time box), 2026-11-09 (DESK-0171, DESK-0210) and 2026-11-10 (DESK-0211).

**Ultracode default (decision 124, 2026-11-14):** substantive work runs as a workflow of subagents with verification stages, at the tier the task deserves, even when that tier is low; the main session briefs and records and keeps its own turns short, because its turns spend the owner's Fable allowance.
