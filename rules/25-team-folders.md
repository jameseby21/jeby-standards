# Team folders: how threads read and write updates

James's rule, 2026-11-08. The jeby team Drive folders are the only channel between the coworker threads (Em, Chaz, Joe, Lily, Bri, Big D), the personal-project chats (Fishing) and Patch (the main Claude Code session). Two problems this fixes: threads re-reading everything on every visit, and updates that name work without the ticket details Desk needs.

## Reading: only what is new
1. Every folder has one pinned document named `00 · Index (newest first)`. Each line is one entry: `date · from · title · tickets: <ids or "none">`. Patch maintains it at every sweep; a thread that writes an entry adds its line at the top.
2. A reader opens the index, finds the last line it has read (it remembers the date and title), and reads only the entries above it. Nothing older is reopened unless an entry says `supersedes: <title>`.
3. When James says "read only the latest unread updates", that is this procedure, nothing more.

## Writing: every entry has the same header
```
Date: 2026-11-08 · From: Chaz · To: Patch (or James, or a thread) · Expires: 2026-11-15
Supersedes: <title of an earlier entry, or none>
Tickets: <ids this entry proposes, updates or closes; or "none">
```
Then one line of context (what James asked), then the body, then the ticket table when work is proposed.

## Ticket-ready items: the table Desk imports
One row per SMART goal, nothing grouped:
`| # | Project | Title (under 60 chars, ask word first) | Type (feature, upgrade, bug, task, docs, decision, research, intake, release) | Size (xs, s, m) | Owner | Assignee | Ask (approve, choose, answer, provide, do, feedback, fyi, none) and by-date | Acceptance (checkable lines) | How to validate (what a person runs or opens, and what they should see) | Depends on | Source |`
A row missing Acceptance or How to validate is filed as `inbox`, not `ready`, and the entry is asked to complete it. Patch posts the real ids back in the same folder within the hour.

## Hand-offs between threads
Assigning work to a thread is a ticket (`assignee: chaz`) plus one entry in that thread's folder carrying the ticket id. The thread delivers as an entry in its own folder with `Tickets:` naming the id; Patch links the delivery to the ticket (`handoff:`), implements what is for Patch, and moves the ticket. James reviews in Desk. James's verdicts are relayed verbatim in the entry, including when he says something looks like shit; the thread answers the verdict, not the tone.

## Files by default, nothing public
Every result a thread produces is also a file in its folder (under Deliverables) or in intake/. Artifact links are views for James, never where work lives. No thread publishes anything publicly.

## Every item has a ticket (James, 2026-11-08)
James: "make it so that any coworker updating the teams file or the tickets will never make that mistake again and ALL items and deliverables get associated to a ticket."
- Nothing a thread produces exists without a ticket id: every entry's `Tickets:` line names at least one real id (never "TBD" or "none" for work); every deliverable file, canvas board, artifact and pull request carries a ticket id in its name, title or first line. A pull request title starts with the id (`JEBYUS-0051: ...`).
- A thread that has work but no id asks Patch for one first, in a one-line entry whose `Tickets:` says `needs id`; Patch files the ticket and answers within the hour. Until then the thread does not post the deliverable.
- Patch's side: an entry, file or pull request without an id is filed as a ticket before anything else is done with it, the thread is told the id, and the miss is a defect in Patch's log, not the thread's.
- Checks: `drew intake --check` refuses an entry whose `Tickets:` is empty, TBD or none when the entry proposes or delivers work; the jeby-us and Desk repositories gain a pull-request check that the title carries an id; the brand register and the Deliverables folders list the id beside every file.

## Updates on demand, not on a clock (James, 2026-11-08)
James: "Let's stop any sweeps -- I will manually prompt when it's time to update or you will be able to tell from changes in tickets" The hourly sweep is retired. Patch reads the team folders when James says so, or when a ticket changes in a way that points at a folder (a hand-off set, a comment that names an entry). Threads keep posting as before; nothing is lost because every item has a ticket (above) and the ticket is the record.

## Outbound: what each thread must look at (James, 2026-11-08)
James: "Coworkers modifying tickets directly is great, but we need a better way to get YOUR results and new tickets out to THEM. I can manually just tell them to check their previously updated/tracked tickets, but then they'd miss out on new ones or re-assigned ones. I certainly can't have them reading ALL tickets. So I guess updates/entries in the team folder in drive is the best way for now -- that way you can simply link tickets to review and each entry can have a list and then be subsequently ignored after going through its items."
- Patch posts, in each thread's folder, an entry that lists exactly the tickets that thread must look at since its last entry: new ones assigned to it, reassignments, and tickets it touched that Patch or James changed; one line per ticket with id, title, status, what changed and the ask. The thread works the list top to bottom and then ignores the entry. Nobody reads all tickets.
- The text comes from `drew outbox --for <actor>` (DESK ticket), which also remembers the cut-off per thread; until it exists, Patch writes the list by hand from `drew list --assignee <actor>` and today's comments.

## Record keeper, not the work (James, 2026-11-09)
- Not every result or response needs an entry, nor every artifact or output file. Work fully described by its ticket (Report, Evidence, a pull request) needs none.
- What is kept strictly, per coworker: the folder's pinned Status and philosophy doc (direction, what James said, dated), hand-offs in and out, and deliverables another person must open; each with a ticket id and an index line.
- The Drive folders are the record keeper; the real work happens through tickets. Ticket creation: anyone proposes a row (Acceptance and How to validate required for ready), Patch files and answers the id within the hour; James creates directly in Desk. Every ticket carries the four roles (rule 27).
- Feedback is part of every role: a coworker speaks up once, with the reason and the alternative, when the direction is wrong or a real improvement exists; otherwise does the ticket. Silence on a known wrong turn is a defect; relitigating an answered point is too.
- New coworkers start from the team README v3 (Drive, jeby team folder, 2026-11-09): roster, what each role needs, common misunderstandings, project-type requirements, the ticket procedure.
