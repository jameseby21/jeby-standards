# Review gates: major work is reviewed by every affected discipline before approval

James's rule, 2026-11-11: "basically ALL major tasks, especially the commercial ones, need a legal, financial, security, creative, UX/UI, and maybe other, reviews before being fully approved.... Therefore they should be subtickets. EVERY UI feature, for example, needs to go through Chaz AND UX AND UI"

- **Major means:** anything commercial (pricing, billing, licences, terms, marketplace listings, contracts, public claims), anything public-facing, and every UI feature.
- **Each review is a subticket** (`parent:` the work ticket, title "Review: <discipline> of <parent title>", type task, size xs). The parent cannot be approved while any review subticket is open.
- **Which reviews:**

| Work | Reviews |
| --- | --- |
| Any UI feature | creative (Chaz), UX, UI |
| Commercial | legal, financial, security, creative |
| Public claim or listing | legal, security, creative |
| Data handling or privacy | security, legal |

- **Default reviewers until James names others:** legal and financial Joe, security Big D, creative Chaz, UX Lily, UI Patch (a checklist of tokens, contrast, focus, 44 px targets and reduce motion, run by an agent and confirmed by Chaz). James changes these in Desk's assign rules (DESK-0168).
- **A review passes** with the reviewer's words in the subticket's Decision. "Not applicable" is allowed only with a one-line reason.
