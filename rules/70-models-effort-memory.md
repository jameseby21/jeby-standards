# Models, effort, memory and the execution queue

Formal, so nobody re-decides it per turn; empowering, so the strongest reasoning lands where judgment is needed and nothing is spent twice.

## 1. Model selection (who thinks with what)

| Role | Model | Why |
| --- | --- | --- |
| Main session (Patch): triage, slicing, decisions, reviews of reports | strongest available (Fable/Opus tier) | judgment, short bursts |
| Project session implementing a ticket | `opusplan` (plans on the strong model, executes on the mid tier); plan mode for anything size `m` | planning is where mistakes are cheapest to fix |
| Subagent `reviewer`, `security-reviewer`, any adversarial verification | strongest allowed for the request | the cost of a missed defect exceeds the tokens |
| The independent checker (skill `qc`) | Sonnet at high effort by default; Opus for judgment-heavy checks; never above the ceiling James set for the request (decision 109) | James, 2026-11-13: ramp it up a little, never Fable |
| `documentor`, `housekeeping` end-of-request checks | cheapest (Haiku) | they file and compare; they do not judge |
| Subagent `doc-sync`, `test-writer`, `slicer`, scaffolding, formatting | mid tier (Sonnet) | mechanical with a spec |
| Read-only exploration, lookups, catalog scans | cheapest (Haiku) or `Explore` | no judgment needed |
| Coworker chat threads (Em, Chaz, Joe, Lily, Bri, Big D) | whatever the thread runs; they produce briefs, never code | |

A subagent inherits the parent model only when the brief says so. A fork (full context) is used only when the task needs the conversation's context; otherwise a fresh agent with a written brief.

## 2. Effort selection

| Effort | Use for |
| --- | --- |
| low | lookups, `drew list`, catalog regeneration, renames |
| medium (default) | ordinary slices, reports, docs |
| high | slicing an intake, a review, a decision brief for James, anything touching money, auth, data integrity or a public push |
| max | only when James or a rule says so (deep multi-agent review); never on a session's own judgment |

State the effort in the subagent brief. If a task turns out to need more, stop and re-brief; do not quietly grind.


## 2b. Ultracode is the standard for subagent work (James, 2026-11-14, decision 124)

> "Let's include 'ultracode' as a standard for subagents even with a lower model/effort.... This is because my fable limits (used for Patch) are running out fairly quickly but the subagents' usage is not being optimized...."

- **Substantive work goes to workflows of subagents by default** (fan out, independent verification, fixers from tests), whatever model tier the task gets; the model and effort table above still picks the tier per task.
- **The main session stays lean:** it decides, briefs, records and reports; it does not read whole files, run long investigations or write large documents itself when a subagent on a cheaper model can. Its own turns are the scarce resource (the owner's Fable allowance).
- **Check:** a pass report states the main session's share of tokens beside the subagents'; a main-session turn that did work a brief could have delegated is a defect.

## 3. Token and context budget

- `CLAUDE.md` under 60 lines per repo; standards live in rules and skills and load on demand; every enabled skill's name costs context each turn, so promotion is a ticket (DESK-0013).
- `/clear` between tickets. Long logs go to files in the scratchpad, named by ticket ID, never into the transcript.
- A subagent or workflow agent runs every test, build and check in the foreground and never ends its turn while something it started is running (lesson 2026-11-10); a result that says it is waiting is treated as not done.
- A subagent brief states: the goal, what is already ruled out, the files worth reading, the scope, the effort, the model, a time box (twice the ticket's upper effort bound; at the box the worker commits what it has, marks unmet lines unmet and reports), and the exact report wanted. Patch sets a wake-up for the box and messages a worker still running at it (lesson 2026-11-08, CONS-0078 worker). If the brief cannot be written clearly, the task is not understood yet.
- One agent per topic at a time. Before spawning, check the ledger (section 5) for a running agent on the same topic; if one exists, wait or message it. Never run inline the work that was delegated.
- A workflow over 50 agents states its expected size and token use before launch, runs early in the week, and checkpoints every agent's result to a file or commit, so a usage limit loses nothing (lesson 2026-11-09: 300 agents, about 27.5 million tokens, weekly limit hit).
- Usage is watched weekly, not hourly: strongest-model work (reviews, slicing) is scheduled early in the week; extra usage is for a deadline, never routine.

## 4. Memory: where a fact lives, written in the same turn it is learned

| Kind of fact | Lives in | Written by |
| --- | --- | --- |
| A process decision | umbrella `DECISIONS.md` | main session, same turn (the `documentor` check confirms the entry exists; it never writes a decision itself) |
| A product or architecture decision | the project's ADR | project session, same ticket |
| Work state (what changed, what ran, what is open) | the ticket's Report | the session that did it, before it stops |
| A lesson (rule + test) | `standards/` (rule, skill, or the cases index) | whoever fixed it, same ticket |
| A durable fact about James, a preference, a correction | Claude Code auto-memory (`~/.claude/projects/.../memory/`) | main session, same turn |
| Personal, family, health, detailed finances | `~/.claude/jeby-private/` only | James, or main session on his say-so |
| Status for coworker threads | Drive "jeby team" folder, dated, with an expiry | main session, weekly |

Chat is not a record. If it is not in one of those places by the end of the turn, it was lost.

## 5. The execution queue for a single request

1. **Parse** the whole request, including late additions mid-turn; final constraints may qualify earlier ones.
2. **Assess** (James's standing rule): reason, logic, resources, convenience, risk. Say in one line what is being done and what is deferred.
3. **Ledger**: a numbered list, each item marked done / in progress / pending / blocked / delegated(agent, topic). Updated every message with tool calls; one edit batch per ledger step so collapsed tool rows map to the ledger.
4. **Reuse check** before any create: a running process, an existing file, a running agent, a prior ticket on the same topic.
5. **Delegate or do**: independent, parallel, or multi-file work goes to agents with written briefs (section 3); a handful of tool calls is done inline.
6. **Checkpoint**: commit, or write the ticket Report, at every natural boundary, so an interruption loses at most one step.
7. **Verify** against the Definition of Done modules the ticket names; mark anything not run as not run.
8. **Record** (section 4), then **report** to James: outcome first, what was not verified, what he must decide.
9. **Close** what was opened (processes, agents, temporary files), and say so. A subagent is stopped by its task id the moment it reports or goes idle; none is left resumable and idle (James, 2026-11-09: "subagents should never be left idle and should forcibly close whenever they're not active").
10. **Report twice, in two sizes.** While work runs, a short update at each milestone. The after-action report (outcome, evidence, how to validate, what was closed) comes once, only when no subagent, workflow or monitor is running (James, 2026-11-09, decision 88).

## 6. Preventing duplicate and lost effort

- Same topic, two places: the ticket wins. If a coworker brief or a chat already has ticketing information, it is imported (DESK-0004), not re-invented.
- An agent's report is pasted into the ticket Report, not left in chat.
- A session that stops without writing its Report is a defect; the Stop hook (M2) refuses it.
- Scratchpad files are named by ticket ID; the ones worth keeping move into `intake/` or the repo before the session ends.
- Two sessions never hold the same ticket (`drew claim` refuses it). Two tickets never describe the same outcome (triage checks `drew list` first).

## 7. Subagents sized to the task, every time (James, 2026-11-11; supersedes decision 89's "max model for all agent work")
James: "regardless of your specific model and effort level, your subagents should be appropriately configured.... I've already spent 25% of my resources in only 2 requests because of you're lack of tact in that regard". Every spawn picks model and effort from section 1 and 2 for that task alone, never by default to the strongest. Mechanical builds with a written spec run on the mid tier at medium effort. Lookups run on the cheapest tier. Only review, adversarial verification and decision briefs get the strongest tier. The brief states both. Patch's report to James names each agent with its model, effort and running time. Before any fan-out of more than two agents, Patch states the planned agents and why in one line. Patch tells James when its own record justifies a model or effort upgrade; it never assumes one.
