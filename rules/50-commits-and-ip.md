# Commits, branches and IP

- Conventional Commits; one conceptual change per commit; no `--no-verify`; no force-push to `main`.
- Branch per ticket: `<project>/<ID>-<slug>`. Merge after `drew decide --approve`, then `drew done --commit <sha>`.
- Every repo carries a LICENSE (MIT for libraries and tools, AGPL-3.0 for hosted apps unless an ADR says otherwise), a copyright line naming the owning entity, and a DCO note for outside contributors.
- Product names are working names until a trademark search and a domain are done.
- Commit and PR attribution lines are whatever the current Claude Code reminder specifies.

## Main is protected (James, 2026-11-08)
James: "Make sure that ALL my branches are protected because while I want as many people using and adding to my repo, I certainly don't want anyone changing the main branch. Make sure that Emily and big D both know that I want research briefs about this for next working sessions"
- Every repository's default branch is protected on GitHub: no force push, no deletion, changes only through a pull request, administrators included. Patch applies it the hour a repository is created; private repositories get it when GitHub Pro is on (MGMT-0007) or when they go public.
- Nobody pushes main, Patch and workers included. A worker pushes its ticket branch and opens a pull request whose title starts with the ticket id; James approves in Desk (or merges on GitHub), then Patch merges.
- Outside contributions arrive by fork and pull request; the contribution model and files are SEC-0010; the security baseline is SEC-0011.
