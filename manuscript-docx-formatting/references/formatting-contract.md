# DOCX formatting contract

## Contents

1. [Authority and modes](#authority-and-modes)
2. [Content-preservation boundary](#content-preservation-boundary)
3. [Style classification](#style-classification)
4. [Natural paragraph construction](#natural-paragraph-construction)
5. [Line and page numbering](#line-and-page-numbering)
6. [Manuscript front matter](#manuscript-front-matter)
7. [Journal-specific formatting](#journal-specific-formatting)
8. [Rendered-page QA](#rendered-page-qa)
9. [Delivery evidence](#delivery-evidence)

## Authority and modes

Use this precedence for journal-specific work:

1. direct editor instructions supplied for the current submission
2. exact official template for the article type and submission stage
3. current official journal author instructions
4. explicit user instructions
5. conservative scholarly manuscript defaults

For generic `format-fix`, do not force a journal intake. Apply the requested
repair plus the global DOCX postcondition and preserve other valid layout. If a
line-spacing token is absent, use `double`; do not inherit Word's 1.08/1.15
default. Use restrained black typography and preserve existing paper size,
margins, fonts, and heading hierarchy unless they are part of the requested
repair or are visibly non-manuscript styling.

For `audit-only`, do not modify the file. Run the inventory, mechanical audit,
and rendered-page inspection, then report exact failures.

## Content-preservation boundary

Before editing, record the source file's SHA-256 and save to a distinct output
path. Treat the following as content, not formatting:

- scientific wording, claims, numbers, equations, and statistical notation
- citation fields, citation order, and reference entries
- figure/table contents, legends, labels, and callouts
- author names, affiliations, declarations, and correspondence details
- comments, tracked changes, bookmarks, cross-references, and embedded objects

Do not intentionally change these in a format-only run. Compare extracted text
before and after, allowing only user-authorized textual differences. If the
chosen DOCX runtime cannot safely preserve a feature, stop before writing or
mark that feature `NOT ASSESSABLE`; do not silently flatten it.

## Style classification

Inventory every distinct style used by a non-empty top-level paragraph. Build
two explicit sets:

- body prose: `Normal`, `Body Text`, or manuscript-specific prose styles
- semantic non-body: title, authors, affiliations, headings, lists, captions,
  bibliography, footnotes/endnotes, headers, and footers

Do not classify paragraphs from their visual appearance alone. A custom style
must be passed to the audit as `--body-style` or `--exclude-style`. If one style
mixes prose and non-prose roles, restyle those roles before auditing. Table-cell
paragraphs are not adjacent top-level body paragraphs.

Use real Word paragraph styles and restrained hierarchy. Unless an official
template requires otherwise, title, headings, subheadings, and body text must
be black. Remove theme-accent blue, decorative paragraph borders, shading,
cards, banners, icons, and report-style layout.

## Natural paragraph construction

For every adjacent pair of top-level body-prose paragraphs, require this Word
structure with formatting marks visible:

```text
body text¶
¶
next body text¶
```

The middle item must be a real empty `<w:p>`, equivalent to pressing `Enter`
twice in consistently styled text. Require exactly one; zero or two-or-more
fails.

For body prose and the empty separator:

- effective space before = `0 pt`
- effective space after = `0 pt`
- `beforeAutospacing` and `afterAutospacing` absent or disabled throughout the
  effective paragraph/style chain
- explicit line spacing equals the resolved token

Do not insert separators around titles, headings, lists, captions, equations,
figures, tables, or bibliography entries. Do not substitute paragraph spacing,
a manual line break (`Shift+Enter`/`<w:br>`), or an empty table row.

This construction is a user-level output invariant, not a claim about every
journal's native style. Record any template conflict instead of bypassing it.

## Line and page numbering

Every section must contain Word-native line numbering with:

- `w:lnNumType`
- `countBy=1`
- `restart=continuous`
- no paragraph-level `w:suppressLineNumbers`

Every active default, first-page, and odd/even header/footer story must contain
an effective dynamic `PAGE` field. A typed numeral, `NUMPAGES`, an inactive
story, or a field in only one section does not count. Remove `w:pgNumType`
restarts so page numbering remains continuous. The journal-neutral position is
the upper-right header. Lower-center or another placement requires an explicit
user choice or recorded current journal/template rule.

Run `enforce_docx_line_page_numbers.py` before the audit. The enforcer writes a
new file by design and refuses to overwrite the input.

## Manuscript front matter

For manuscript drafts, apply the separate semantic and visual contract in
[front-matter-contract.md](front-matter-contract.md). Inventory title, authors,
affiliations, correspondence, Abstract, and Keywords before repair. Prefer
explicit Word styles; when a draft uses the same style for several roles, pass
one-based top-level paragraph numbers to the normalizer and audit rather than
guessing from appearance.

Run the front-matter normalizer before the numbering enforcer, then run both the
whole-document structural audit and the front-matter audit. The manuscript
profile does not apply to cover letters, response letters, or supplements that
do not have a manuscript title block.

## Journal-specific formatting

When the user explicitly requests a journal format, record a compact checklist
with one row per applicable rule:

| Field | Meaning |
|---|---|
| `category` | page, font, spacing, numbering, section order, anonymization, references, tables/figures, declarations, or package |
| `rule` | exact current requirement |
| `source_url` | official source or supplied-template path |
| `accessed` | access date |
| `implementation` | concrete DOCX action |
| `verification` | mechanical or visual check |
| `status` | `PASS`, `FAIL`, or `NOT ASSESSABLE` |

Confirm the exact journal, article type, and submission stage. Initial
submission, revision, accepted manuscript, and proof stages can differ. Do not
reuse another article type's template or an old publisher-wide profile as
current proof. If official sources cannot be inspected, continue only with the
global invariant and label journal-specific compliance `NOT ASSESSABLE`.

## Rendered-page QA

Render every page after the mechanical audit. Inspect at readable zoom:

- black title and heading hierarchy
- clipping, overlap, missing glyphs, and broken equations
- margins, page breaks, orphan headings, and excessive whitespace
- tables, captions, figure placement, and references
- headers/footers and visible continuous page numbers
- visible continuous line numbers on text-bearing pages
- anonymous-review requirements and unintended metadata display

Re-render after every layout-sensitive correction. Mechanical XML checks do
not replace page inspection.

## Delivery evidence

Deliver:

- a new formatted DOCX, never the overwritten source
- a JSON mechanical audit showing `MECHANICAL_PASS`
- for a manuscript, a JSON front-matter audit showing `FRONT_MATTER_PASS`
- rendered visual-QA status: `PASS` or `NOT ASSESSABLE`
- content-preservation status based on an extracted-text comparison
- the resolved line-spacing token and body/non-body style classification
- for journal mode, the source-linked checklist and any invariant/template
  conflicts

Do not call the file “journal compliant” if a mandatory journal check is
`FAIL`/`NOT ASSESSABLE`, or “fully verified” if page rendering was not inspected.
For manuscripts, combine the structural, front-matter, preservation, journal,
and render gates with `validate_format_release.py`; only
`FORMAT_RELEASE_PASS` closes the resolved formatting contract.
