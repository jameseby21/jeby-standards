---
name: gps
description: Run before acting on any request or writing any ticket: Goal in one sentence, Proof of what good looks like and how to tell, Steps without handwaving. James's "jeby-reality" check for Patch (from Sandeep Swadia), trained on the ticket store, with per-project overrides.
---

# GPS: Goal, Proof, Steps

Pairs with `follow-through`: GPS says what the work is and how to know it is done; follow-through carries it to that proof. Used by `common-sense` on every request.

James's rule (2026-11-09), adopted from Sandeep Swadia ("You're Not Behind (Yet): Learn AI Agents in 13 Minutes", 2026-05-14):

> Since you (Patch) are my main "employee" and "delegating assistant" and "CTO/CPO", your main "jeby-reality" check is GPS (idea taken from Sandeep Swadia): "goal" -- can I define the goal very clearly in one sentence?, "proof" can I tell what 'good' looks like and how will I know if the agent got it rght?, and "steps" can I describe each step clearly without handwaving? I want this formalized for ALL requests, but also I want it to be flexible enough so that I can modify it for my own specific requirements within ANY project

Swadia's warning behind it: an agent "doesn't fix bad thinking, it formalizes it".

## Goal

- **One sentence with a verb that names who or what ends up where.** Default limit 30 words; 40 for `decision` and `research` tickets.
- **In a ticket, the goal is the bold lead line of Outcome** (`**Goal.** ...`); bullets below it are not counted.
- **Fails:** a noun fragment ("Its own mark, replacing the admin template."), the title restated, a pointer elsewhere ("per its hand-off", "as described in the brief"), two goals joined by "and" or semicolons (split it into two tickets).
- **A decision ticket's goal is the question with its options.**

## Proof

- **A line is observable when it names an instrument and an observation.** Instrument: a command in backticks, a URL, a file path, a place to open (page, board, folder, calendar, Decision, Report), or a named person's words in Decision. Observation: what it shows, with a value (prints `0 files differ`, returns true, lists five rows, event on 2027-03-15, the entry names this id, James's words approving).
- **Proof passes when Acceptance plus How to validate hold at least one observable line** and no acceptance line is a template phrase.
- **Blacklist (found in the store):** "shipped as described", "to be written", "works" alone, "complete" alone, "tests pass" without a test name, "done or inapplicable", "profile filled", "looks good", "if James says so".
- **An Acceptance made only of past participles fails** ("Rule added", "Templates checked", "Test"): those are activities, not observations.
- **Tickets created before 2026-11-08** (before How to validate existed) are scored from Acceptance alone and warn, never error, until their backfill lands (DESK-0232).

## Steps

- **At least one step names an action and an object that appears in the Outcome or Acceptance.**
- **Not steps:** reading the ticket, its source or a brief (a preamble); a routing note such as "Worker (Sonnet, medium): desk repo" (a header).
- **Handwaving phrases (found in the store):** `run the checks`, `do the step`, `report drift`, `the rest`, `as described`, `per its hand-off`, `if James says so`, `or inapplicable`, `do only what Acceptance names`, `something`, `everything`, `attempt`, `try to`, `stuff`, `if needed`, `TBD`, `etc.`, `and so on`, `figure out`, `somehow`, `as needed`, `as appropriate`. Words such as check, verify, implement, update, review are fine when the step names its object.
- **Decision and do tickets pass with two steps:** who answers where, and who records where ("James answers in the reply box; Patch records").

## Where it lives

- **Requests:** Patch's first update on a new request carries one GPS line per goal; a goal that cannot pass becomes one question to James, with a recorded default when the choice is reversible (`not-a-blocker`).
- **Tickets:** Outcome opens with `**Goal.** ...`; Acceptance and How to validate carry observable lines; Prompt is `**Steps.**` with a numbered list. `drew new` and the batch writers produce this shape (DESK-0233). The models: DESK-0212 to 0215, MGMT-0012 to 0016, SCI-0001 to 0003, CONS-0081, STD-0046.
- **Subagent briefs:** every brief opens with Goal, Proof and Steps (standards rule 70 lists what else a brief carries).
- **Desk check:** `drew validate` scores each letter per ticket (DESK-0215).

## Per-project overrides

A project's profile may carry a `gps:` block. Keys: `goal_max_words`, `proof_requires` (any of `command`, `url`, `file`, `ui`, `decision`, `source`, `test`, `date`), `extra_handwaving`, `allow`, `steps_min`, `by_type` (overrides keyed by ticket type). Proposed blocks (STD-0048):

- **Research projects** (cosmology, science-stats, nfl-analytics, writing, prompting): `goal_max_words: 40`, `proof_requires: [source, file]`; "explore" is allowed only with a stopping rule.
- **Design work** (brand, showcase, Chaz's tickets): `proof_requires: [file]`, James's words in Decision as the observer; `extra_handwaving: [polish, tweak, refresh, modernize, "clean look", "make it pop"]`.
- **Personal projects** (life, fishing, tutoring, philanthropy, temujin): `goal_max_words: 20`, `proof_requires: [date]` or James's word in Decision; `steps_min: 1`.
- **Money and legal** (funding, consulting pricing, terms): `proof_requires: [source]`; `extra_handwaving: ["reach out", network, pitch, negotiate]` unless the step names the party and the channel.
- **jre:** `proof_requires: [test]` (a named test file and its pass line).

## Applied

- 2026-11-10: James's request of 2026-11-09 evening split into thirteen goals, each filed as a ticket in GPS shape.
- 2026-11-10, training pass over 1,466 tickets (STD-0046, intake/2026-11-10-gps-training.md): the first heuristic agreed with a careful reader on Goal 32 of 40, Proof 28 of 40, Steps 30 of 40; the rules above replace it. Proposed scoring moves the store from G 1,268 / P 222 / S 1,345 / all 111 to G 1,087 / P 328 / S 952 / all 164.
