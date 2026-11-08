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
