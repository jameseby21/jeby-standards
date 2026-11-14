# analyses

The nine analysis files of standards rule 29 exist and each ends in a determination.

- [ ] `docs/analyses/` holds market.md, competitors.md, customers.md, financial.md, legal.md, licensing-ip.md, security-privacy.md, brand-design.md and operations.md.
- [ ] `grep -L -E "^Determination: (not applicable|nothing to report|suggestions|warnings|blockers)" docs/analyses/*.md` prints nothing.
- [ ] No determination is past its review-by date, or the stale ones are named in the Report.
- [ ] Any file whose determination is `blockers` names the decision ticket that settles it.
