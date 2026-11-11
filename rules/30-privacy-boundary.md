# Privacy boundary

- Personal, family, health and detailed financial context lives only in `~/.claude/jeby-private/` and in the main session's conversation. It never enters a project repo, a ticket, a commit, a coworker brief or a subagent prompt. Translate to business terms: "a family investor", "variable capacity".
- Real source data stays in the owner's vault, never in a repository, not even an ignored folder.
- Secrets live in a password manager or in `.env` files that are gitignored. `Secure docs/` is never committed.
- Student data, minors, account numbers and ID numbers never enter any repo or Drive folder.
- Each public edition of a project is swept for private strings before its first push.

## Stricter, by default (James, 2026-11-11)
James: "let's be even way more strict on this because I lack experience here but it's vital". Additions:
- **Identifying details count, not only names.** An employer, a neighbourhood, a relationship, a pronoun that narrows a small group, a health word or a real company tied to a person all identify. Use a role ("the beta design partner") and "they".
- **A private-strings scan runs before every commit** in the umbrella and in every project repo. `standards/scripts/private_scan.py` reads a denylist kept only in `~/.claude/jeby-private/denylist.txt` and refuses the commit when a staged line matches. The denylist is never committed.
- **Outside AI tools (Gemini, ChatGPT and the like) are outside parties.** What James pastes into them is his call. Anything that comes back is quarantined in his private Drive folder until it is cleaned, and only the clean copy enters Desk or a team folder.
- **A "Confidential" label is not protection.** Documents are written as if they will be forwarded.
