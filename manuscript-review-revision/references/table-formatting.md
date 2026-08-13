# High-standard manuscript tables

Load this contract whenever a manuscript contains, creates, revises, formats,
or audits a table. Resolve table content, typography, rules, and rendered layout
as separate surfaces.

## Authority and scheme resolution

Use this order:

1. a specific editor instruction;
2. the exact current article-type and stage template;
3. the current official journal guide;
4. the journal-neutral three-line fallback below.

Read the complete source sentence. Example-only wording does not override the
fallback. Record `table_rule_scheme`, `table_rule_basis`,
`table_rule_strength`, and `table_rule_source_excerpt` in the journal format
plan. Use `preserve-official` only when a binding/direct source or exact
template resolves a scheme that the normalizer must not replace.

## Journal-neutral three-line fallback

For every editable Word table:

- keep only a top rule, a rule below the header row, and a bottom rule;
- use no vertical rules, outer side rules, internal body gridlines, colored
  fills, zebra bands, decorative borders, or report-style accents;
- make the first row a bold header and repeat it across page breaks;
- top-align cell content;
- use the resolved manuscript font, 10 pt cell text, single line spacing, and
  0/0 pt paragraph spacing;
- keep the table title/caption at body size and manuscript line spacing;
- keep the table editable; never replace it with a screenshot or flattened
  image.

The bundled normalizer implements this as `--table-rule-scheme three-line`.
The semantic-rhythm audit must receive the same expected scheme. A current
official full-grid rule may use `full-grid`; a more specialized exact template
uses `preserve-official` plus source-linked plan and visual checks.

## Content and statistical table gate

Do not silently invent, delete, or reinterpret content during formatting.
Inspect every table for:

- a unique table number and concise, self-contained title in the required
  location;
- column headings that state variables and units;
- consistent decimal precision, percentage denominators, missing-value
  notation, and alignment of comparable values;
- sample size and analysis population where needed;
- named effect estimates, uncertainty intervals, exact or appropriately
  reported P values, statistical tests, and multiplicity handling where
  applicable;
- defined abbreviations, symbols, superscripts, significance markers, and
  footnotes;
- consistency among the table, manuscript text, figure/legend, source data,
  and statistical output;
- no blank spacer rows/columns, duplicated headers, split labels, clipped
  values, orphaned titles/notes, or unexplained color encoding.

If a content defect cannot be repaired without scientific judgment, mark the
table gate `FAIL` or `NOT_ASSESSABLE` and request the required author decision.
Do not make a formatting pass conceal a data or statistical defect.

## Render and release gate

Render every page at readable zoom after the final table change. Inspect all
tables for width, wrapping, row splitting, repeated headers, rule visibility,
caption/note attachment, page breaks, superscripts, symbols, and grayscale
legibility. Mechanical XML checks do not replace this inspection.

Every table must pass resolved-scheme structure, typography, content/statistics,
cross-artifact consistency, and rendered-page gates. One failing or unassessed
material table blocks a table-format pass and therefore blocks final DOCX
release.

Record the aggregate result for each delivered manuscript as `table_status` in
`07_format_audit.json`, together with the resolved table font size, line-spacing
token, and rule scheme. A journal format audit cannot pass unless these values
match the current format plan and `table_status=PASS`.
