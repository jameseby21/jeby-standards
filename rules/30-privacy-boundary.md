# Privacy boundary

- Personal, family, health and detailed financial context lives only in `~/.claude/jeby-private/` and in the main session's conversation. It never enters a project repo, a ticket, a commit, a coworker brief or a subagent prompt. Translate to business terms: "a family investor", "variable capacity".
- Real source data stays in the owner's vault, never in a repository, not even an ignored folder.
- Secrets live in a password manager or in `.env` files that are gitignored. `Secure docs/` is never committed.
- Student data, minors, account numbers and ID numbers never enter any repo or Drive folder.
- Each public edition of a project is swept for private strings before its first push.
- Data a tool takes from users is screened before it is processed: licensed identifiers, personal data, minors, credentials and unlawful content are excluded by default or never processed. The classes, the default and the overrides are in [35-data-screening.md](35-data-screening.md).
