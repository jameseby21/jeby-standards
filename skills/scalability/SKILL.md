---
name: scalability
description: Judge any structure, process or tool by what happens at ten times its size (more tickets, projects, companies, coworkers, files, users or rows). Use when designing or reviewing a folder tree, a ticket hierarchy, a data layout, a process with a manual step, or anything whose cost grows per item, and when James writes $scalability. Pairs with reproducibility; the reviewer subskill of QA/QC applies both.
---

# Scalability: it still works at ten times the size, without a rewrite

**Pairs with `reproducibility`.** Scalability asks whether it still works when there is ten times more of it. Reproducibility asks whether someone else gets the same result from the record alone. A structure that scales but cannot be redone drifts. One that can be redone but does not scale gets redone by hand forever. The `reviewer` subskill of QA/QC applies both.

> "assesses established structure vs. goals to ensure proper $ scalability" (James, 2026-11-13)
>
> "This also requires the infrastructure to handle cross-company or cross-project items, but that falls in line with our philosophy of total generality and modularity anyway." (James, 2026-11-13, decision 109)

## Rules

1. **Name the multiplier.** State what grows (tickets, projects, companies, coworkers, sessions, files, rows, users) and its count today, from a command.
2. **Find the cost per item.** Any step done by hand per item (per ticket, per project, per coworker) is the first thing that breaks. Count the hand steps, then multiply by ten.
3. **No level is hard-coded.** A level of a hierarchy (company, project, track) is data, not a constant in code or a folder name baked into a tool. Decision 99: the hierarchy can change, so it is handled natively and testably (skill `modularity`).
4. **The general form, with the case as data.** A rule, field or tool that names one project, one partner or one person is a special case. Prefer the general form and keep the case in data (decision 109, "total generality and modularity").
5. **Views are bounded.** A list, board or report that shows everything at once breaks at ten times. It needs grouping, paging or a default filter (decision 79, the broad-context board).
6. **Budget the hot path.** For a tool, name the operation run most often and its time today and at ten times (`drew bench` for the ticket store).
7. **One place per fact.** Copies multiply drift with size. Link to the owner of a fact instead of copying it (rule 20).

## Check before done

- The multiplier and today's count are stated, with the command that counted it.
- Each hand step per item is listed with its count at ten times, or the reply says there is none.
- No new level, project, partner or person is hard-coded where data would do.

## Applied

- 2026-11-13: one route-to-market ticket with a row per project (MGMT-0050) instead of 36 tickets; one secrets ticket from two proposals (SEC-0018); a merge that lists every project it came from (DESK-0263, `also_projects`) instead of one project per ticket.
