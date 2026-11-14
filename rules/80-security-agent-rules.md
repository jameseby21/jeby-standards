# Security work: standing rules for any agent

From Big D's security baseline (2026-11-08), adopted as a standard. Security is proportional: a project gets what its class (A to E, in its profile) needs and no more. A free, open-source project with no accounts and no private data builds no logins.

1. Scans and audits are read-only. Never rotate credentials, rewrite git history, force-push or delete anything unless the ticket says so and James approved it.
2. Never print, store or send a secret value. Reports are masked and show file, commit and type. If a command would reveal a real value, stop and tell James.
3. Never ask James for a password or key in a ticket box; reply boxes refuse secret-looking values.
4. Do not create accounts, enter credentials or change money-moving settings. Those are `do` steps for James.
5. Install tools outside the repo, from official sources, with checksums verified. Ask before anything that needs admin rights.
6. Proof lists the exact commands that ran and where, and names what was not run.
7. File findings in the project's findings folder and update the owning docs through the docs index.
8. A secret that was ever committed, pasted into a chat or intake file, or synced to a shared place is exposed: recommend rotation and let James decide.
9. Public repos: scan before the first push; secret scanning and push protection on; CI must pass before merging to main; releases built by CI with checksums; a SECURITY.md (jeby alias, not a personal address) and a license in every public repo.
11. **No one acts as anyone** (James, 2026-11-13, decision 110: "NO ONE (except maybe the real human me) should EVER be able to "ACT AS" anyone until further notice"). No agent, coworker or tool posts, signs or decides as another person. Relaying someone's words is stamped as a relay with the words quoted (`--relaying`, DESK-0261). The check: no record a session wrote names anyone but that session as its writer.
10. Local tools with a web UI (Desk) bind to this computer only and refuse requests from other origins; no login is added where there is nothing to protect.
