# Thread and session protocol: nine rules (DRAFT)

**DRAFT, pending DESK-0157 (the Desk MCP server). Not imported by `INDEX.md` and not in force.** James approves the rule and its entry in `INDEX.md` after the server exists; until then rule 25 (team folders) is the channel. Source: Lily's entry of 2026-11-08 (LILY-30 to LILY-39, ticket STD-0042).

Applies to every chat thread (Em, Chaz, Joe, Lily, Bri, Big D), Patch, and every Claude Code session. Desk is the one place where work is said, claimed, done and decided. Tool names below are the proposed Desk MCP tools and may change when DESK-0157 settles them.

1. **Inbox first.** At the start, call `desk_inbox` with your actor name and read only what it returns. It advances your cursor; `peek` does not.
2. **Search before create.** Call `desk_search` first. If a ticket already covers the work, comment there.
3. **Create with a `dedupe_key`.** Use `desk_create` with a key such as `lily:2026-11-08:desk-mcp`. The same key twice returns the existing ticket. A likely duplicate needs `confirm_new` and a stated reason.
4. **Claim before work.** Use `desk_claim` (a lease, renewable). A ticket claimed by someone else is refused with the claimant's name and the lease end. This is the same claim as in rule 10.
5. **Progress as comments.** Progress, questions and findings are `desk_comment`s on the ticket, never only in a chat.
6. **Hand off by assignee.** Change the assignee and comment why; the new assignee sees it in their inbox.
7. **Decisions are tickets.** A decision is a ticket of type `decision`; `DECISIONS.md` is generated from them.
8. **Only James approves.** The MCP tools cannot approve, reject, delete or mark a ticket done with evidence. Those stay in the Desk UI.
9. **Documents stay in Drive or the repos** and are linked from the ticket.

## Each actor names itself
A thread's project instructions state its actor (`patch`, `lily`, `chaz`, `em`, `bri`, `joe`, `bigd`, `james`, or `code:<project>` for a project session). Every write records the actor and its source.

## Hooks that enforce two of the rules
- **SessionStart** prints the session's inbox before anything else (rule 1).
- **Stop** refuses to end a session that holds unticketed work (rules 2 and 3 in spirit: nothing happens outside a ticket).

## What changes in other rules when this is approved
- Rule 25 (team folders): Drive stops being the message bus and keeps documents; the hourly sweep and the `00 · Index` documents retire after the proof ticket (LILY-39) passes.
- `10-slice-contract.md`: unchanged; claims and Reports already live in tickets.

## Open until approved
- The final tool names and the lease length (DESK-0157).
- How web and mobile chats reach Desk (LILY-38) and the inbox for threads that cannot run a local server (DESK-0116, DESK-0159).
- The READ ME v3 text for the jeby team folder and each thread's actor line.
