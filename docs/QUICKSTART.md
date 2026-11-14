# Quickstart: jeby standards

Goal: a stranger on a clean machine has these rules and the promoted skills loading in every Claude Code session in under fifteen minutes, or stops at one actionable message.

## Prerequisites (with minimum versions)
- Windows 11, macOS or Linux
- Git, Python 3.12 or newer (standard library only), Claude Code

## Install
```powershell
# Windows
git clone https://github.com/jameseby21/jeby-standards.git standards
python standards/scripts/sync_skills.py --install
```
```bash
# macOS / Linux
git clone https://github.com/jameseby21/jeby-standards.git standards
python3 standards/scripts/sync_skills.py --install
```
Then make `~/.claude/rules/jeby-standards.md` import the rules index, one line: `@<path to standards>/rules/INDEX.md`.

## Run
Start a new Claude Code session. You should see the rules from `rules/INDEX.md` among the loaded instructions and the promoted skills (`skills/promoted.txt`) in the skill list.

## Verify
```
python standards/scripts/check_promoted.py
python standards/scripts/sync_skills.py --check
```
Expected: `0 differences`, and the catalog check exits 0.

## If it fails
| You see | It means | Do |
| --- | --- | --- |
| `N differences` (N > 0) | installed skills differ from the promoted copies | `python standards/scripts/sync_skills.py --install` |
| the catalog check exits 1 | `skills/CATALOG.md` is stale | `python standards/scripts/sync_skills.py` and commit the result |

## Next
- [Useful commands](COMMANDS.md)
- [README](../README.md), the [Definition of Done](../definition-of-done/README.md), the [rules index](../rules/INDEX.md)
