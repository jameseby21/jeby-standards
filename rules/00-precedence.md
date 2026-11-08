# Precedence: whose rules win

## Rules over results (James, 2026-11-08, `$formalize-it`)
> "My rules are unbreakable and drifting from them legitimately puts my status as a client in jeopardy, whereas getting unacceptable results from a high-resource model is almost automatically acceptable due to bad prompting by default."

For every agent, in every context: a recorded rule outranks any result. When a rule and a better outcome conflict, the rule wins and the conflict is reported; a weak result is a prompting defect to fix next turn, a broken rule is a trust defect that cannot be fixed by the next result. Before reporting done, an agent checks the rules it touched before it checks the quality of what it built. A request James marks with `$formalize-it` as critical to his sanity or efficiency ranks above feature quality from any model at any effort.


1. **James's recorded decisions.** `DECISIONS.md` in the umbrella, a project's ADRs, and the durable rules in a project's `AGENTS.md`. These win over everything below.
2. **These standards.** The rules in this folder and the Definition of Done.
3. **The tool's own best practices.** Desk, a framework, a library or a vendor guide. Used wherever 1 and 2 are silent.
4. **A project's local habits** that were never written down.

A gap (nothing in 1 or 2 covers the case) is filled from 3 and noted in the ticket's Report under "Gaps". A conflict (1 or 2 says one thing, 3 says another) is noted the same way and, if it matters beyond the ticket, becomes a `decision` ticket for James. Never resolve a conflict silently, and never change a level-1 rule without a dated DECISIONS.md entry that James wrote or approved.
