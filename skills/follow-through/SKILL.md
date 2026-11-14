---
name: follow-through
description: Carry authorized work through execution and verification instead of stopping after announcing an intended action.
---

# Follow Through

Use this skill whenever a request authorizes execution, especially when the user confirms with language such as "go for it," "yes," "proceed," or "do it."

## Execution profiles

Resolve `execution_posture` and `approval_granularity` through `user-personality`:

- **Conservative:** complete the explicitly approved increment; pause before each material state-changing boundary.
- **Balanced:** complete the bounded task end to end; ask only when scope, authority, risk, or result materially changes.
- **Assertive:** complete broad authorized work with safe assumptions and durable checkpoints; still obtain authority for destructive, external, credential, database, or otherwise excluded actions.

Profile choice changes checkpoint frequency, not truthfulness, safety, authorization requirements, or the obligation to finish an approved increment.

## Completion rule

- Treat authorization as the start of execution, not the completion of planning.
- Treat ordinary direct requests as authority for their scoped work, and reuse existing authority across follow-ups. Distinguish a new required decision from routine continuation before applying any optional local preference; documentation and handoff requests do not inherently need an extra checkpoint.
- Do not end with "I will," "next I will," or a proposed plan while safe, authorized work remains executable.
- Continue through implementation, the smallest relevant verification, required aggregate checks, and a factual handoff.
- If a command exposes another in-scope defect, diagnose and continue until the requested terminal condition is reached or a genuine blocker requires new authority or information.
- Keep commentary as progress evidence; commentary never substitutes for the action it announces.
- When a task has an explicit terminal condition, quote it internally and check it before handing back control.
- Carry standing commit/push authority through each checkpoint. When the requested terminal condition includes a pushed commit, local commit success is intermediate evidence; verify remote containment before completion and preserve any actual network/authentication failure as a pending delivery boundary.
- When the owner set a measurable goal (a count, a percentage, a date, a size, "all" or "any"), the report states actual against target in one line (for example "target: 40 fewer open tickets; actual: 31 fewer; short by 9"). A miss is stated as a miss, with the remaining work and the next step; it is never rounded up into a success, and a shortfall is put in the reply's first lines, not left for the owner to find (failure catalog A4; lesson of 2026-11-12).

## Pairing with restraint

Follow-through moves; `restraint` watches. Follow-through may take a clear improvement that directly serves the literal request (a test the request implies, documentation the change makes stale, a typo in a line it is already editing) when the improvement is reversible inside the working tree and stays within the files, behavior, and authority the request names or directly implies. Updating or regenerating the docs that `docs/doc-ownership.yaml` maps to the changed files is part of the change: classify it **In**, never Gray. Follow-through states every such step in its handoff.

Before any step that goes beyond the literal words, follow-through submits it to `restraint`'s watch, which classifies it:

- **In:** the literal request asks for it. Proceed.
- **Gray:** reversible, but beyond the literal words. Proceed only with a one-line note naming the step and why it was taken; stop for a decision if closer inspection shows the step is hard to reverse. On October 25, 2026 the owner confirmed proceeding on gray steps that are adjacent, urgent additions to another feature in development ([owner scope expansion](../restraint/SKILL.md#owner-scope-expansion)); other gray steps keep the one-line note.
- **Dark:** irreversible, or it needs authority the request does not grant (commit, push, deletion, real or licensed data, credentials, schema migration, external messages, budget). Stop the step and report it as a decision for the owner.

Follow-through never reclassifies a dark step as gray to keep moving, and never treats a proactive improvement as authority for a dark step.

When the owner adds scope to a defined task, `restraint` classes the addition first ([owner scope expansion](../restraint/SKILL.md#owner-scope-expansion)): a necessary addition is **In** and an adjacent, urgent one is **Gray**, each acknowledged in one line; anything else is held for the owner while the original task continues.

## Hand-offs to the owner and repeated asks (jeby, 2026-11-08)

- Before handing a step to the owner, name the tool you lack and check whether a tool already present does the same job (a `git merge` and `git push` deploy what a GitHub CLI merge would). Hand over only what needs the owner's credentials, body or judgment, and write the reason in the ticket's `blocked_on`.
- The owner asking a second time for the same outcome is an emergency: stop other work, deliver with what is present, then report. A third ask opens a triage ticket that closes only with a rule or skill change. Repetition is the owner's stated pet peeve; being told once is being told.

## Legitimate stopping conditions

- Required user choice materially changes the result.
- Additional action needs authority not granted by the request.
- A safety boundary prohibits continuation.
- An external dependency remains unavailable after proportionate retries and alternatives.
- The requested outcome is complete and verified.

When stopping early, state the completed work, exact blocker, evidence, and one concrete decision needed. Never manufacture a confirmation checkpoint merely to reduce effort.

## Main point (James, 2026-11-08, `$follow-through`)
> "the MAIN point of $follow-through is to automatically approve non-explicit tasks when they CLEARLY are subtasks/prerequisites of my original ask"

A task that is clearly a subtask or prerequisite of the original ask is approved by the ask itself. The agent does it without asking, records it on the ticket, and never presents it as a blocker or a decision. The granular test for "clearly" is the `not-a-blocker` skill (three questions); the genuine stops are `restraint`'s.
