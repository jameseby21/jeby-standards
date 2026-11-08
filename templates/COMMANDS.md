# Useful commands: <project name>

Every command a person or an agent runs day to day, with what it does and when. Keep it current: a command that no longer exists is a defect.

## Daily
| Command | What it does | When |
| --- | --- | --- |
| `<run>` | starts the app | every session |
| `<test>` | runs the focused suite | before every report |
| `<lint / format>` | | before every commit |

## Data and environment
| Command | What it does | Notes |
| --- | --- | --- |
| `<migrate>` | | never edit a shipped migration |
| `<seed / fixtures>` | | synthetic data only |
| `<reset>` | | destructive: says so and asks |

## Build, release, docs
| Command | What it does | Notes |
| --- | --- | --- |
| `<build>` | | |
| `<docs check / regen>` | | generated blocks are never hand-edited |
| `<release>` | | CI builds; checksums published |

## Desk
| Command | What it does |
| --- | --- |
| `drew next --project <key>` | the next ready ticket for this project |
| `drew claim <ID>` / `drew report <ID> --file report.md` | take a ticket; hand it back with proof |
| `drew snap <ID>` | attach a screenshot as evidence |

## Troubleshooting one-liners
| Symptom | Command |
| --- | --- |
| port in use | `<how to find and stop your own process by PID>` |
| stale install | `<how to reinstall / drew doctor>` |
