# Precedence: whose rules win

1. **James's recorded decisions.** `DECISIONS.md` in the umbrella, a project's ADRs, and the durable rules in a project's `AGENTS.md`. These win over everything below.
2. **These standards.** The rules in this folder and the Definition of Done.
3. **The tool's own best practices.** Desk, a framework, a library or a vendor guide. Used wherever 1 and 2 are silent.
4. **A project's local habits** that were never written down.

A gap (nothing in 1 or 2 covers the case) is filled from 3 and noted in the ticket's Report under "Gaps". A conflict (1 or 2 says one thing, 3 says another) is noted the same way and, if it matters beyond the ticket, becomes a `decision` ticket for James. Never resolve a conflict silently, and never change a level-1 rule without a dated DECISIONS.md entry that James wrote or approved.
