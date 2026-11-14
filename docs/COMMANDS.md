# Useful commands: jeby standards

Every command a person or an agent runs day to day, with what it does and when. Keep it current: a command that no longer exists is a defect.

## Daily
| Command | What it does | When |
| --- | --- | --- |
| `python scripts/sync_skills.py` | rebuilds `skills/CATALOG.md` and `skills/catalog.json` | after adding or changing a skill |
| `python scripts/sync_skills.py --install` | also copies promoted skills into `~/.claude/skills/` | after pulling a new version |
| `python scripts/sync_skills.py --check` | exits 1 when the catalog is stale | hooks and CI |
| `python scripts/check_promoted.py [--skills-dir DIR]` | prints each difference between promoted and installed skills, then `N differences`; exit 1 when N > 0 | before reporting a skill change |
| `python scripts/private_scan.py` | refuses a staged diff that adds a private term (rule 30) | before every commit |
| `python scripts/private_scan.py PATH ...` | scans whole files | before publishing a file |
| `python scripts/private_scan.py --self-test` | proves the matcher with a temporary denylist | after changing the scanner |

## Build, release, docs
| Command | What it does | Notes |
| --- | --- | --- |
| edit, bump `VERSION`, tag | a release of the standards | see [Updating](../README.md#updating) |

## Desk
| Command | What it does |
| --- | --- |
| `drew next --project <key>` | the next ready ticket for this project |
| `drew claim <ID>` / `drew report <ID> --file report.md` | take a ticket; hand it back with proof |
| `drew snap <ID>` | attach a screenshot as evidence |
