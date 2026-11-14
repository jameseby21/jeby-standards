# jeby standards

The shared way every jeby project is built. Public, MIT. Three things live here:

| Folder | What it is | How it reaches a session |
| --- | --- | --- |
| `rules/` | Always-on prose standards, short, one topic per file. `INDEX.md` imports them all. | `~/.claude/rules/jeby-standards.md` imports `INDEX.md`, so every Claude Code session on the machine loads them. Codex reads `AGENTS.md` in each repo, which links here. |
| `definition-of-done/` | The modular Definition of Done. `core.md` always applies; a ticket names the other modules in its `dod:` list. | Desk tickets carry `dod: [core, code, docs]`; reviewers check the named modules. |
| `skills/` | The skills library. `CATALOG.md` is generated from every project repo; `promoted.txt` names the ones installed globally. | `scripts/sync_skills.py --install` copies promoted skills into `~/.claude/skills/`. |

Later (Desk milestone M2): a Claude Code plugin in this repo (`.claude-plugin/`) with the hooks, agents and the `drew` binary (the Desk CLI), installed once per machine at user scope.

Start here: [docs/QUICKSTART.md](docs/QUICKSTART.md); every command: [docs/COMMANDS.md](docs/COMMANDS.md).

## Precedence
When a project's own conventions, these standards and a tool's built-in best practices disagree, the order is in `rules/00-precedence.md`: James's recorded decisions win, then these standards, then the tool's defaults, and every conflict is written down rather than silently resolved.

## Updating
Change the file, bump `VERSION`, tag. Desk opens one `task` ticket per machine to pull and re-run `sync_skills.py --install`. Nothing about standards is pasted into prompts again.
