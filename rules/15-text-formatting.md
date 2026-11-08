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
