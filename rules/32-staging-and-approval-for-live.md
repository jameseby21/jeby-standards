# Staging for everyone, one approval for live

James's rule, 2026-11-13 (decision 117):

> "within reason, all my coworkers should be empowered to submit changes to test and include them as test features in staging, but should have a hard, thorough, complete. but easily-pushed, "approval for live" option from my end. This feature ensures maximum "confident and seemingly obvious" changes while also allowing me a seamless way to revert and modify them, regardless of any other forks/branches/edits/suggestions/changes/modifications/upgrades/etc made along the way...."

> "This obviously comes with strict but permissive definitions at the start (that I have to review manually as a first step) but then expand to be more blanket and philosophical as a true CEO/founder/chairman role SHOULD evolve...."

## The two tiers

| Tier | Who may put a change there | Gate | Where it shows |
| --- | --- | --- | --- |
| **Staging** | any coworker or worker, inside their domain | the basic security check (SEC-0020) and the project's tests, run by the tool, no human step | a staging address per site or tool; a "test feature" flag per change, so several can sit side by side |
| **Live** | James only, by one action | the release ticket, which shows everything in one place (below) | the live site or the installed tool |

## Approval for live: hard and thorough, one step

- **One release ticket per candidate** (type `release`), filled by the tool, never by hand: what changed (one line per ticket it carries), the diff size, the test results, the security check output, the staging address and screenshots, the people who signed each domain, and the exact revert command.
- **One action:** James approves the release ticket (`drew decide --approve` or its button). Nothing else is asked of him. A "changes requested" sends the candidate back to staging with his words on the ticket.
- **Every live release is an immutable artifact** (a tag plus the built files or the installed version), kept forever. Revert is one command to any earlier release, and it redeploys the stored artifact rather than rebuilding, so it works regardless of what branches, forks or later edits exist.
- **Modify after the fact:** James's change request on a live release opens a staging candidate automatically, linked to the release it modifies.

## "Within reason": the first definitions (strict, reviewed by James first; STD-0066)

Staging is open to a coworker's change when all of these hold:

1. it is inside the coworker's domain (decision 108);
2. it passes the basic security check and the project's tests;
3. it moves no money, creates no account, changes no credential, and exposes no private data or individual-level record;
4. it adds no third-party origin, dependency or licence without a line in the release ticket;
5. it is flagged as a test feature so it can be turned off without a deploy.

Anything outside these waits for James. The list is reviewed by him first and is widened by dated decisions as the role matures.

## The check, before reporting done

- Every live change in a pass report names its release ticket, its artifact tag and its revert command.
- `drew release list` (DESK-0266) shows every live release with its tag; the newest is what the live address serves.

## Applied

- 2026-11-13: the first live pushes under decision 114 (jeby.us, jainsights.com) carried the security check and a revert commit but no release ticket or artifact tag; DESK-0266 and the per-site staging tickets bring them under this rule.
