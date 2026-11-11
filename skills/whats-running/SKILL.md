---
name: whats-running
description: Priority rule (James's sanity; outranks feature quality). Before any message names a URL, port, preview, server, build, branch, installed tool or version, state what is running, where, which version, who started it and whether the reader must start something, check every link answers, and put any step the reader must run inside How to validate. Repeat it every time.
---

# What's running

**Priority marker: critical to James's sanity and efficiency.** This rule outranks feature quality from any model at any effort (standards rule 00). A report that is right about the feature but wrong about what is running is a defect.

> "If you need me to run/do ANYTHING in order to validate, then that should be part of the "How to Validate" details....." (James, 2026-11-11)

> "If you are running/hosting/serving/expecting different versions of things, make that FUCKING CRYSTAL CLEAR to me even if you have to repeat yourself.... "Repetition" is a pet peeve of mine, sure, but me having to hear repetition is NOTHING compared to me having to repeat myself...." (James, 2026-11-11)

**Case:** a ticket link pointed at port 8766, a preview that had already stopped. James's own Desk on 8765 worked when he changed the port by hand.

## The rule

**Every agent that names a running, hosted, served or versioned thing says, in that same message:**

| Say | Example |
| --- | --- |
| what it is and its version | Desk 0.2.0, installed, commit a77e496 |
| where it is | http://127.0.0.1:8765, or C:\...\dist\index.html |
| who started it and when | your drew-ui from your VS Code terminal; or Patch, PID 1234, at 14:05 |
| whether it is the same as what the reader usually uses | yes, it is your normal Desk; or no, it is a preview of a branch that is not merged |
| what the reader must run if it is not up | the exact command, inside How to validate |

**When two versions exist at once** (installed and a preview, main and a branch, live site and a local build), name both. Say which one each link opens, every time, even if the last message said it.

## Checks before sending

1. **Every localhost or preview link answers.** Run `curl -s -o /dev/null -w "%{http_code}" <url>` and get 200 (or the expected code) in the same turn. A link that does not answer is either removed or given its start command.
2. **Links point at what the reader runs,** not at an agent's own preview, unless the message says so.
3. **How to validate starts with any step the reader must run.** For example, "Start Desk if it is not running: `drew-ui` in a terminal (it serves http://127.0.0.1:8765)", followed by the checks.
4. **Every process the agent started and leaves running is listed** with port, PID and version. Every process it stopped is listed too.
5. **Repeat it.** The reader's memory of an earlier message is not a source; restate the state in each message that relies on it.

## Words for the levels

The hierarchy can change, so a skill or a tool reads the levels from the current definition (DECISIONS.md, latest entry on the hierarchy) and never hard-codes them. As of 2026-11-11:

- **empire:** jeby, jeby.us and the umbrella brand;
- **company:** a business entity;
- **project:** a specific, open-ended product line that a company offers;
- **product:** anything packaged, public or private, free or monetized.

## Applied

- 2026-11-11: the LIFE-0015 link failed (port 8766 was down). The following message names Desk on 8765 (James's drew-ui) with its version, after a curl check, and How to validate starts with the drew-ui step.
