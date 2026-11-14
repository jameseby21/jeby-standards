---
name: not-a-blocker
description: Before anything is labelled a blocker or a decision, test whether it is simply a prerequisite or subtask of the original ask (pre-approved by follow-through) or a thing an agent can create with a present tool; only James's credentials, body, money or a non-defaultable judgment block. A granular skill used by common-sense and bounded by restraint.
---

# Not a Blocker

Used by `common-sense` as its granular check on anything about to be called a blocker, a dependency or a decision. Bounded by `restraint`, which names the genuine stops. Fed by `follow-through`, whose main point is that non-explicit tasks are approved automatically when they are clearly subtasks or prerequisites of the original ask.

James's definition (2026-11-08): "'[x] had no home.' is never a valid excuse or reason. ... having no home is literally only another missing ticket not a blocker. ... it deals only with ideas that you might be inclined to label as 'blockers' or 'decisions' when in reality they are simply requirements of the main request and pre-approved through $follow-through."

Use this skill every time an agent is about to write `blocked_on`, "waits on", "depends on a decision", "was not defined", "nobody had ticketed", or to hand a step to James.

## The three questions, in order

1. **Is it a prerequisite or subtask of what was asked?** A board that opens at companies needs a company level; a company level needs profiles; profiles need a list. Each is part of the ask. Follow-through pre-approves it: do it, do not ask.
2. **Can the missing thing be made with a present tool?** A ticket, a profile, a file, a record, a default name, an ordering, a mapping, a test fixture. Then it is work, not a blocker: make it, record it, continue.
3. **Does it truly need James's credentials, his body, his money, or a judgment that cannot be defaulted and reversed?** Only then write `blocked_on`, and name which of the four it is. Privacy, destructive actions, public pushes and merges he reserved stay his (restraint).

## Default and proceed

When a choice is needed but reversible (a name, a list, an order, a threshold), pick the obvious default, write it on the ticket as an assumption with the date, and continue. A decision ticket may exist beside the work so James can rename or regroup later; it never blocks the work. Renaming is a refinement, not a scope change.

## Phrasings that fail the check

"had no home", "nobody had ticketed", "was not defined", "waits on a decision" (for a reversible choice), "needs a design first" (when the design ticket is already filed and the model or data half can proceed), "the tool does not exist" (before checking whether a present tool does the job, rule 10). Each is rewritten as the action taken: "filed as X", "defaulted to Y, recorded on Z".

## Checks

- Every `blocked_on` names one of: credentials, body, money, non-defaultable judgment, or a real external dependency (a certificate, a merge James reserved, another person's delivery).
- No explanation of a gap appears without the ticket or file that closed it in the same sentence.
- Reversible choices show a recorded default, not a waiting state.
- The report's "waiting on James" list has been run through the three questions; items that fail are moved to work.
- Before any question to the owner, search `DECISIONS.md` and the standards rules for an answer he already gave (`grep -n -i "<key words>" DECISIONS.md`, and the rules folder). If one exists, the answer is applied and cited by its decision number, and the question is not asked. A feature or record that breaks a standing rule is reported as a breach with its fix, never put to the owner as a question (failure catalog D6; lesson of 2026-11-13, DESK-0261).

## Applied

- 2026-11-08: Patch wrote "The hierarchy had no home" and blocked the company level (DESK-0181), Chaz's design (DESK-0182) and the company board (DESK-0183) on a naming decision (DESK-0180). Corrected the same turn: the proposed company list is the default, the three tickets are unblocked, the decision ticket stays for renaming only.

Pairs with `executive-decisions`, which carries the ladder of who may decide what once a thing is shown not to be a blocker.
