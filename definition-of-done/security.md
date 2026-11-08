# security

- [ ] Scans and audits were read-only; no secret value is printed, stored or sent (rules/80-security-agent-rules.md).
- [ ] No secret, key or token in the diff, the ticket, the Report or a log; `.env` files are gitignored.
- [ ] A tool that takes user data screens it first and excludes or refuses flagged classes (licensed identifiers, personal data, minors, credentials, unlawful content) as in rules/35-data-screening.md; a test per class, including `td_linxID` as the licensed-identifier example.
- [ ] Nothing flagged is logged, stored or sent; the output names what was left out and why.
- [ ] A local web UI binds to this computer only and refuses other origins.
- [ ] A public repo was scanned before its first push and carries SECURITY.md and a license.
