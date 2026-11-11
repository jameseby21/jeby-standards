# Text formatting ladder: longer text, stricter shape

James's rule (2026-11-08), from a ticket whose Context was a wall of text: text fields follow general formatting guidelines where more characters mean more stringent requirements, and very large generated text is saved as markdown, not pasted into a field.

| Length of a field | Required shape |
| --- | --- |
| under 300 characters | one or two plain sentences |
| 300 to 1,200 | short paragraphs; a quotation on its own line; ids and commands in backticks |
| 1,200 to 4,000 | a bold lead sentence per paragraph, or a bulleted list; at most one quotation block; links instead of pasted text |
| over 4,000, or any generated output | saved as a markdown file (intake/ or the project's docs) and linked from the field, which keeps a three-line summary |

- Context says why the ticket exists in the first sentence; the rest is evidence, quoted and dated.
- A field that renders as one block of more than twelve lines is a defect (`drew validate` warns; the UI shows a readability flag).
- Quotations from James are kept verbatim but set as quotations, with the date, never run into Patch's own sentences.

## No plain block of text (James, 2026-11-09)
> Use this also as an opportunity to make ALL text formatted in a much nicer, prettier format, even with markdown tags and stuff like that. I don't want to see a plain block of text in any ticket.

- Every free-text section (Context, Outcome, Prompt, Out of scope, Report, Evidence) opens with a bold lead when it holds more than two sentences, then one bullet per sentence or tight pair; a quotation of James sits on its own blockquote line after its attribution.
- A plain block is a prose paragraph over 300 characters, three or more sentences over 200 characters without a bold lead, or a bullet over 400 characters. Quotations, code and tables never count.
- `drew validate` warns on every plain block (DESK-0209); the 2026-11-09 cleanup (DESK-0210) reformatted the store under a checker that keeps every word.
- Ticket ids and file paths stay out of backticks so Desk can link them; backticks are for commands.

## Human-readable by default, everywhere (James, 2026-11-11)
James: "Your tickets need way better explanation. Make sure the explanations of issues (and everything else too) follow human-readability standards because this is garbage on that front. And I mean across the entire app, not just any specific tickets...."

Every piece of text a person reads (tickets, reports, Desk screens, buttons, empty states, errors, docs, chat replies) follows plain-language practice (plainlanguage.gov, the US Federal Plain Language Guidelines; ISO 24495-1):
1. **Lead with the point in everyday words:** what is wrong or being asked, then why it matters to the reader, then what happens next and what they will see.
2. **Write for a smart reader who was not there.** Target reading grade 8 or lower (Flesch-Kincaid) for explanations; 10 at most for technical detail.
3. **Short sentences, one idea each.** Average under 20 words; active voice; "you" for the reader.
4. **No unexplained jargon or shorthand.** Rule numbers, internal words (bone, lane, ask, slice, DoD, fixture, ADR, flush), abbreviations and metaphors get a plain gloss on first use or are replaced. An id never stands alone: "BSA-0011 (how you will test the add-in)".
5. **Screens say what things are.** Labels name the thing ("Claimed tickets"), buttons name the action ("Approve"), errors say what happened and what to do. Mascot or metaphor wording ("In your mouth", "Fetched") may appear only beside a plain label, never instead of one.
6. **Check before done.** `drew validate` warns on ticket fields above grade 10 or with a listed jargon word unexplained (DESK-0253); a UI change lists its new or changed strings in the Report with their grade.
