---
name: management
description: "Balances the parts of the business for the owner: it pushes attention to the backlog when it is too urgent or too large, keeps room for planned improvements at any time, and stops future development from going too far while recording every detail of it. Every new feature or project gets its smallest shippable slice defined before anything else. Use at the start of every pass and every weekly review, whenever a new idea arrives, and when the owner writes $management. Pairs with ideal-trajectory; uses executive-decisions, release and gps."
---

# Management: the right lane for every piece of work, and an MVP before anything else

> "I'm only one person with a lot of good ideas who can't seem to prioritize MVPs for new features/projects..... let's get started on a $management skill, which tries to balance out ALL the different necessary portions of a business in a reasonable way for me. In other words: it forces me (or tries to) to focus on backlog items when they are too urgent/voluminous, but also allows me to make planned improvements at any time, while preventing me from going too far on (yet still perfectly recording all details regarding) future development" (James, 2026-11-14, decision 125)

Not a hard rule, by his words: a balance the skill keeps unless he overrides it, and every override is recorded.

## 1. The four lanes

| Lane | What belongs there | Budget of a week's attention (default) | What may happen to it |
| --- | --- | --- | --- |
| **Now** | p0 and emergencies, overdue asks, failing live things, security, money that is stuck | takes what it needs first | built and shipped before anything else |
| **Planned** | the sprint's committed improvements, each with an MVP slice | about 60 percent of what is left after Now | built in slices; one slice per session |
| **Later** | ideas and future development, fully recorded | at most 10 percent, spent on recording, never on building | a ticket in inbox with GPS, options, risks and the MVP slice named; no code, no design beyond a sketch |
| **Parked** | what the owner decided not to pursue now | zero | the record stays; a dated line says why |

The budgets are data (`desk.toml`, `[management]`), not constants, and the owner changes them with a dated decision.

## 2. The signals that move the balance (read from the store, never estimated)

- **Now is too urgent** when any of: p0 or emergency tickets open; an ask to the owner overdue; a live site or installed tool failing a check; a second ask for the same thing (rule 10).
- **Now is too voluminous** when: created minus closed over the last seven days is positive by more than the sprint's capacity; or the review queue's oldest item is older than seven days; or open tickets per owner exceed the cap in `desk.toml`.
- **The balance is healthy** when Now is empty of emergencies and the created-versus-closed line is flat or falling.

`drew stats` and `drew validate` give the numbers; the weekly review ticket shows them as the dashboard.

## 3. What the skill does with a new idea (the MVP rule)

1. **Record it fully, the same day**, as one ticket in inbox: the owner's words, the goal in one sentence (gps), the options, the risks, who it serves, and the nine analyses it will need (rule 29). Nothing is lost by waiting.
2. **Name the smallest shippable slice** before any other work: one outcome, one person can finish it in one focused session or one week, and a real user can touch it. The rest becomes rows under the parent, in Later.
3. **Place it:** if Now is too urgent or too voluminous, the slice waits in Later with its date; if the balance is healthy, the slice may join Planned; it never jumps to Now unless it is money stuck, a security hole or a live failure.
4. **Stop the drift:** a Later ticket gets no worker, no branch and no design file; a session that finds itself building one stops, records what it learned on the ticket, and returns to Now or Planned.

## 4. What the skill does for the owner each pass and each week

- **Opens with the balance:** Now (count, oldest), Planned (slices this week, done so far), Later (new ideas recorded), created versus closed, and the one MVP slice it recommends he ships next.
- **Forces focus when Now is red:** the pass works Now first and says so in its first line; new ideas are recorded and not built; the owner is told in one line what he has to clear before Planned work resumes.
- **Allows planned improvements any time Now is green:** the owner may pull any Planned slice forward without ceremony; the skill only asks that it be a slice.
- **Prevents going too far:** when Later work is touched for more than the budget, the pass report says so as a miss (follow-through, actual against target), with the hours and the ticket.
- **Records every override:** the owner may say "build it now"; the ticket gets a Decision line with his words and the lane it skipped, so the pattern is visible in the weekly review.

## 5. Where it lives

- `desk.toml` `[management]`: lane budgets, caps per owner, the review-age threshold, the sprint capacity.
- The weekly review ticket (project management, the MGMT weekly) carries the dashboard and the list of overrides.
- Desk shows the lane on the board as a column filter and on each ticket (DESK ticket to follow; until then `tags: lane:now|planned|later|parked`).

## Checks before done

- Every new idea recorded this pass has an MVP slice named and a lane tag.
- The pass report opens with the balance line and names the one slice to ship next.
- No Later ticket has a branch, a worker or a design file; any time spent on Later is reported against the budget.
- Every override by the owner has a dated Decision line.

## Applied

- 2026-11-14: Florida Man recorded fully (FLMAN-0001 to 0005) with no build, lane Later; the three sites and the sales data were Now; the hierarchy and staging rules were Planned; the review found 425 tickets created against 12 closed since 2026-11-10, which is the "too voluminous" signal this skill exists for.
