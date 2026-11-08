---
name: ideal-trajectory
description: Translate agreed project priorities into bounded development stages, dependencies, validation gates, and durable handoffs for immediate and longer-term work; the partner of chunked-delivery.
---

# Ideal Trajectory

Pairs with `chunked-delivery`. Ideal trajectory keeps the SMART queue and its order; `chunked-delivery` lands each queue entry as a verified checkpoint. A plan with no checkpoints is a wish, and checkpoints with no queue drift.

Use when an agreed direction needs a concrete delivery plan or existing plans need realignment. Do not reopen settled goals merely to generate a plan.

## Planning contract

- Use the project's current roadmap and documentation hierarchy rather than creating competing sources of truth. In jeby work the queue is Desk tickets (`desk board`, `desk next --project <key>`) and the slice contract is `standards/rules/10-slice-contract.md`.
- Maintain new actionable work as SMART queue entries (tickets). Link roadmap commitments and wishlist ideas to that queue; preserve active and completed work as evidence rather than retroactively creating goals. Record queue state separately from any native Goal state, and activate only an explicitly requested Goal supported by the available tools.
- Require all five SMART criteria: Specific outcome; Measurable acceptance evidence; Attainable scope with available inputs and authority; Relevant product or user value; Time-bound target or review deadline. Include dependencies, owner, affected boundaries, iteration policy, and a concrete failure and recovery stop condition. A time estimate alone is not a deadline.
- Distinguish the immediate authorized increment, dependencies, future committed scope, and optional ideas. Preserve the user's chosen commit boundaries unless a concrete blocker requires a decision.
- Define each stage by outcome, affected surfaces, evidence required, and completion or escalation condition. Separate implementation time from external waits and uncertain debugging.
- Treat estimates as ranges with assumptions and confidence. Do not invent account telemetry, exact credit costs, delivery guarantees, or cross-platform success.
- Estimate inspection, implementation, verification, documentation, and commit and push effort together. Separate hands-on effort from network, build and approval waits. Use recent comparable work when available; otherwise label the range provisional and low confidence. Split work too uncertain for a reviewable checkpoint into discovery followed by implementation. For an active session, set the first review within 30 minutes; later queued work gets a review date and is re-estimated when activated. If the upper estimate is exceeded or a dependency changes, update the range and rationale without weakening acceptance criteria.
- Inspect native Goal status before claiming activation or a reset. Create failures, usage limits, and absent reset timestamps are evidence; elapsed time or cumulative tokens alone do not identify their cause. Do not mark an unfinished Goal complete to free a slot. Keep any unavailable native action visible while progressing authorized queue and document work.
- Choose the smallest useful verification for each change while retaining explicit aggregate gates. Two consecutive successful runs mean the same required suite on the same source state; record revisions and do not imply older results validate new executable changes.
- Put safe authorized work into execution through `follow-through`; a plan is not a substitute for implementation.
- If the user leaves or rests, finish authorized work and leave a durable handoff (the ticket Report) without inventing new permissions. Do not make urgency or fatigue a reason to skip tests or expand destructive authority.
- Place observations and unresolved items in the ticket Report, committed work in the roadmap, and speculative improvements in the wishlist. Do not rewrite archival evidence.

## Validation

Check that every immediate outcome has an evidence gate, dependencies precede consumers, estimates expose uncertainty, and unresolved approvals are explicit. Distinguish documentation readiness, application test results, manual acceptance, and clean-clone and platform validation.
