# Commits, branches and IP

- Conventional Commits; one conceptual change per commit; no `--no-verify`; no force-push to `main`.
- Branch per ticket: `<project>/<ID>-<slug>`. Merge after `desk decide --approve`, then `desk done --commit <sha>`.
- Every repo carries a LICENSE (MIT for libraries and tools, AGPL-3.0 for hosted apps unless an ADR says otherwise), a copyright line naming the owning entity, and a DCO note for outside contributors.
- Product names are working names until a trademark search and a domain are done.
- Commit and PR attribution lines are whatever the current Claude Code reminder specifies.
