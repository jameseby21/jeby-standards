---
name: gps
description: Run before acting on any request or writing any ticket: Goal in one sentence, Proof of what good looks like and how to tell, Steps without handwaving. James's "jeby-reality" check for Patch (from Sandeep Swadia), with per-project overrides.
---

# GPS: Goal, Proof, Steps

Pairs with `follow-through`: GPS says what the work is and how to know it is done; follow-through carries it to that proof. Used by `common-sense` on every request.

James's rule (2026-11-09), adopted from Sandeep Swadia ("You're Not Behind (Yet): Learn AI Agents in 13 Minutes", 2026-05-14):

> Since you (Patch) are my main "employee" and "delegating assistant" and "CTO/CPO", your main "jeby-reality" check is GPS (idea taken from Sandeep Swadia): "goal" -- can I define the goal very clearly in one sentence?, "proof" can I tell what 'good' looks like and how will I know if the agent got it rght?, and "steps" can I describe each step clearly without handwaving? I want this formalized for ALL requests, but also I want it to be flexible enough so that I can modify it for my own specific requirements within ANY project

Swadia's warning behind it: an agent "doesn't fix bad thinking, it formalizes it"; a vague goal drives the car "straight into the tree faster and with more confidence".

## The check, every request and every ticket

1. **Goal.** One sentence, under about 30 words, naming who gets what. If it takes two sentences, the request is two goals: split it.
2. **Proof.** What good looks like and how to tell, observable by someone other than the author: a command and its output, a page and what it shows, a person's words in a Decision. "It works" or "looks good" is not proof.
3. **Steps.** Each step names an action and its object. No handwaving: "handle", "deal with", "clean up", "improve", "optimize", "figure out", "as needed", "as appropriate", "etc.", "and so on", "various", "relevant", "somehow", "make sure it works", "TBD". Replace each with the concrete action, or make it a question.

## Where it lives

- **Requests:** Patch's first update on a new request carries one GPS line per goal. A goal that cannot pass is a question for James, asked once, with a default when the choice is reversible (`not-a-blocker`).
- **Tickets:** Goal is the first sentence of Outcome (written as "**Goal.** ..."); Proof is Acceptance plus How to validate; Steps are the Prompt's numbered steps.
- **Subagent briefs:** every brief opens with Goal, Proof and Steps sections (standards rule 70 lists what else a brief carries).

## Per-project overrides

A project profile may carry a `gps:` block that changes the defaults, for example:

```yaml
gps:
  goal_max_words: 40
  proof_requires: [command, screenshot]
  extra_handwaving: ["tweak", "polish"]
  allow: ["as needed"]
```

Defaults: `goal_max_words: 30`; Proof needs at least one acceptance line and one how-to-validate line that names what to run or open and what to see; the handwaving list above. `drew validate` applies the project's block (DESK-0215).

## Checks

- One-sentence goal present and under the limit.
- Proof names an observable check and who or what observes it.
- Steps contain no word from the handwaving list (project overrides applied).
- A failing letter is fixed before work starts, or becomes one question to James.

## Applied

- 2026-11-10: James's request of 2026-11-09 evening split into thirteen goals, each filed as a ticket written in GPS shape (MGMT-0012 to 0016, DESK-0212 to 0215, CONS-0081, SCI-0001 to 0003, STD-0046). The training pass over the store (STD-0046) sets the defaults from real tickets.
