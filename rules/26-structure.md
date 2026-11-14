# Structure: one tree, everywhere, applied recursively

James's rule, 2026-11-13 (decision 111). Names are replaced in brackets here, as rule 30 requires:

> "a folder called "[the partner company]" should be fucking shared with [the partner company] ([its contact]) as basic $ common sense and should be within jeby Industries > JA Insights > Partner Projects > [the partner company] > Distributors&Importers. How many times do I need to tell you to structure things correctly? Apply proper structure to EVERYTHING related to jeby Industries -r"

## The tree

- **Every jeby item lives at one path in one tree:** jeby Industries > company > Projects or Partner Projects > project or partner > sub-project. The levels are the hierarchy of decision 99 (empire, company, project, product), and they can change: a level is data, not a hard-coded name (skill `scalability`).
- **The tree is the same on every store:** this computer, the work Drive, the personal Drive and Secure docs. A store that cannot hold an item (a repository, a secret) says where the item lives instead, in its READ ME.
- **Nothing is loose.** An item outside the tree, or at the top of a Drive, is a defect. Moves carry an undo log (skill `reproducibility`).

## Names imply audience

- **A folder named after a partner, client or person is shared with them, and holds only what they may see.**
- **Internal material about them lives in a sibling named "<name> - Internal (private, never share)"**, which is never shared. Both folders carry a READ ME saying which they are (James, 2026-11-13: "Labeling will be important").
- **Secrets never live in a shared folder.** The owner's personal Drive may hold a backup of secrets in its own labelled folder (James, 2026-11-13: "My personal SHOULD include secrets though, for the record, because it is a true backup unlike git"); a secret found inside a shared or partner-named folder is moved to that backup folder, never deleted and never shared further (rule 80 item 8 for rotation).

## The check, before reporting done

- **Before creating a folder or file, state its full path from the root of the tree.** A path that skips a level, or a partner-named folder that is not shared with that partner, is fixed before reporting.
- **Before telling James to share a folder,** list what is inside it and confirm every item is meant for that audience.

## Applied

- 2026-11-13: the personal Drive's partner-named folder held internal material and a folder of secrets. It was renamed "Internal - <name> (personal backup, never share)"; the shared partner folder is built on the work Drive with the partner-facing set only (MGMT-0051, MGMT-0047, SEC-0018).
