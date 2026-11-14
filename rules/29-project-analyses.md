# Project analyses: every project carries a determination for every concern

James's rule, 2026-11-13 (decision 116):

> "Every single project or idea in my library seems to need further competitor & market & customer profiles & financial & legal & others analyses.... Let's make that a formal, blanket idea across my entire brand, so much so that even a new LLM on a new instance on a clean clone of any project even with no experience will have those kinds of analyses. Sometimes, their reports will be "nothing to report" because maybe legal or security aren't necessary for a small private personal project, but the point is that we receive a determination of it rather than dismissing the check entirely."

> "for any project that is proposed either by myself or by a user of my products, should automatically have the proper documentation structure for ALL of these scalable concerns, regardless of whether they're required or not. [...] he/she will automatically have research documents about the legality/financial/licensing/patent/IP implications of the idea whether they are simply suggestions or warnings/blockers."

## The concerns (one file each, in every project's `docs/analyses/`)

| File | Concern | Default owner (rule 28 reviewers) |
| --- | --- | --- |
| market.md | market: size, timing, trends, who else serves it | Joe, Em |
| competitors.md | competitors and substitutes: who, how they charge, what they miss | Em |
| customers.md | customer profiles: who buys, who uses, who pays, their words | Em, Joe |
| financial.md | money: costs, prices, path to a first dollar, break-even | Joe |
| legal.md | legal: contracts, terms, liabilities, regulated data, jurisdictions | Joe (a lawyer decides anything binding) |
| licensing-ip.md | licences in and out, patents, trademarks, originality (rule 55) | Joe |
| security-privacy.md | security class A to E, private data, threat model (rule 80) | Big D |
| brand-design.md | name, marks, voice, how it looks beside the other products | Chaz |
| operations.md | what runs, who runs it, what repeats (decision 94) | Bri, Lily |

## The rule

- **Every project has all nine files from its first commit**, created from `standards/templates/analyses/`. A project with no repository keeps them in the umbrella under its project folder.
- **Every file ends in a determination,** one of: `not applicable` (with the reason), `nothing to report` (checked on a date, nothing found), `suggestions`, `warnings`, `blockers`. "Not applicable" and "nothing to report" are determinations; an empty file or a missing file is a defect.
- **Each determination carries** a date, who made it (a person, a coworker thread or an agent, named as such), the sources read, and a review-by date. A determination older than its review-by date shows as stale.
- **A blocker stops the work it names** until the owner or the named reviewer decides, through a `decision` ticket.
- **The tools make it automatic:** a new project in Desk, a new repository from the standards template, and every project a user generates with AppForge get the nine files with their templates (DESK-0264, FORGE-0037).
- **The Definition of Done module `analyses`** checks the nine files exist and each ends in a determination; a `release` cannot pass without it.

## The check, before reporting done

- `ls docs/analyses` lists the nine files; `grep -L "^Determination:" docs/analyses/*.md` prints nothing.
- No determination is past its review-by date, or the stale ones are named in the report.

## Applied

- 2026-11-13: rollout across the 36 projects is MGMT-0055 (one ticket, one row per project); the first determinations are written by workers from the record and signed by the default owners.
