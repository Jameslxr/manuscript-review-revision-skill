# Formal submission-manuscript formatting

## Contents

1. [Source precedence](#source-precedence)
2. [Submission manuscript visual contract](#submission-manuscript-visual-contract)
3. [Manuscript front matter](#manuscript-front-matter)
4. [Literal body-paragraph separation](#literal-body-paragraph-separation)
5. [Continuous line and page numbering](#continuous-line-and-page-numbering)
6. [DOCX workflow](#docx-workflow)
7. [Submission-package files](#submission-package-files)
8. [Output separation](#output-separation)
9. [Mechanical audit boundary](#mechanical-audit-boundary)

## Source precedence

Apply:

1. specific editor instructions
2. exact journal template for the relevant article type and stage
3. current official journal author guide
4. conservative scholarly manuscript defaults

Initial submission, revision, final submission, and proof correction can require different files and styling. Never reuse a profile from another stage without refreshing it.

Before editing, load and validate the source-linked
`01a_journal_format_plan.json` described in
[journal-format-plan.md](journal-format-plan.md). Confirm its target journal,
article type, stage, and `journal_profile_sha256` against the current run. Do
not format from a generic house style or an older journal profile.

Load [journal-typography-resolution.md](journal-typography-resolution.md) and
classify the complete official font and line-spacing sentences. Do not treat
`e.g., 10-point Times Roman` or other example-only wording as a binding 10 pt
rule.

## Submission manuscript visual contract

Unless an official template explicitly requires otherwise:

- use black title, author block, headings, subheadings, and body text
- use restrained scholarly typography
- use real paragraph styles redefined to the journal profile
- do not use Word theme-accent blue headings
- do not use report covers, colored bands, cards, callout boxes, icons, dashboards, decorative rules, branding, or oversized title treatments
- do not use tables as layout containers
- do not place audit statuses or reviewer notes inside the clean manuscript
- preserve conventional scientific section hierarchy
- when typography is unspecified or example-only, use Title 15 pt bold and
  every other visible manuscript paragraph 12 pt; use 12 pt bold for section
  and subsection headings and preserve their supplied capitalization

The review report may use tables for issue tracking, but its visual system must never be copied into the submission manuscript.

## Manuscript front matter

Load [front-matter-contract.md](front-matter-contract.md) for every manuscript
DOCX. When no current exact journal template resolves a different token, use
the restrained journal-neutral profile: left-aligned title, authors,
affiliations, author notes, correspondence, and ORCID/identifiers; Times New
Roman; one resolved manuscript-wide line-spacing token; body-sized author,
affiliation, author-note, correspondence, ORCID, Keywords, heading, and
declaration text; 1-inch margins; top vertical alignment; no table, text box, centered
display block, or decorative container. Use explicit role styles or one-based
paragraph numbers after inventory; never infer author identities from visual
appearance.

Place exactly one real Enter-created empty paragraph between every adjacent
present block in this order: Title, Authors, Affiliations, optional Author notes,
Correspondence, optional ORCID/identifiers, and Abstract. Keep consecutive
paragraphs within one block compact. This semantic block-gap matrix has no
journal-template bypass unless the user explicitly changes the personal
house-style invariant.

Run `apply_manuscript_profile.py` before the numbering enforcer, then run
`audit_docx_front_matter.py` and `audit_docx_semantic_rhythm.py` separately from
the whole-document structural audit. A journal-sourced override may change alignment, typography,
anonymization, title-page location, or page-number placement, but must be
recorded in the validated format plan and checked explicitly.

## Literal body-paragraph separation

Use this invariant for every modified DOCX:

- Set the effective `spaceBefore` and `spaceAfter` of every body-prose paragraph to `0 pt`.
- Remove or disable `beforeAutospacing` and `afterAutospacing` in paragraph and body-style OOXML; a visible `0 pt` value does not close the gate while automatic spacing remains enabled.
- Resolve body line spacing as an exact manuscript token. Use the exact journal/template value when specified; otherwise use `double` as the conservative review-manuscript fallback. Never inherit Word's default `1.08`/`1.15` line spacing and never disable this check.
- Insert exactly one structurally empty paragraph between adjacent body-prose paragraphs. In Word with formatting marks visible, the structure is `body text¶`, `¶`, `next body text¶`.
- Give the empty separator paragraph effective `spaceBefore=0 pt`, `spaceAfter=0 pt`, and the same line-spacing token as the surrounding body style. This is the structure produced by pressing `Enter` twice in consistently styled body text.
- Use real semantic styles: `Title`/author/affiliation, `Heading`, `Normal` or `Body Text`, `Caption`, `List Paragraph`, and `Bibliography` as applicable. Do not style title blocks, lists, captions, or references as body prose merely to obtain spacing.
- Do not substitute `spaceAfter`, `spaceBefore`, CSS/HTML margins, or a manual line break (`Shift+Enter`, `<w:br>`) for the empty paragraph.
- Do not insert body separators around list items, captions, figures, tables,
  equations, or bibliography entries. For manuscript semantics, require exactly
  one real empty paragraph before a new section, subsection, or declaration
  heading; none between a heading and its first body paragraph; none before
  Keywords; and exactly one after Keywords.
- Treat CRediT entry paragraphs as a dedicated semantic non-body role. Load
  [credit-authorship-contract.md](credit-authorship-contract.md), require
  recognized official role vocabulary, and keep consecutive author entries
  compact with no empty paragraph between them.

When authoring OOXML directly, the separator must be a real empty `<w:p>`
between the two body `<w:p>` elements. When using a document library, create an
empty paragraph in the body style and explicitly set its before/after spacing
to zero. Do not rely on inherited Word defaults.

This paragraph construction is a personal output invariant, not a journal
default. Apply it to every modified DOCX. If an exact journal template
conflicts, record the conflict in `01_journal_profile.json` and
`07_format_audit.json`; do not bypass the invariant or claim simultaneous
template compliance.

## Continuous line and page numbering

Apply this invariant to every modified DOCX, including manuscripts, tracked
copies, clean copies, cover letters, response letters, and editable
supplementary text:

- set `w:lnNumType` in every section to `countBy=1` and
  `restart=continuous`;
- remove every paragraph-level `w:suppressLineNumbers` instruction;
- add a dynamic Word `PAGE` field to the default page story in every section;
- when `different first page` or odd/even headers and footers are enabled, add
  an effective `PAGE` field to those active stories too;
- remove page-number restarts after section breaks so numbering remains
  continuous;
- do not count a typed numeral, a `NUMPAGES` field, or a page field present only
  in an inactive header/footer story as page-number coverage.

Use the bundled enforcer before the mechanical audit:

```bash
python3 "$SKILL_ROOT/scripts/enforce_docx_line_page_numbers.py" \
  manuscript.docx --out manuscript.numbered.docx
```

If a journal template conflicts, keep the user invariant, record the conflict,
and do not claim simultaneous template compliance.

## DOCX workflow

1. Preserve the original.
2. Validate `01a_journal_format_plan.json`; stop with `NOT ASSESSABLE` when a mandatory plan item is unresolved.
3. Use the journal template when required; otherwise create the explicit style map recorded in `style_contract`.
4. Apply every plan check in order, including stage-appropriate fonts, margins, spacing, line numbering, anonymization, section order, citations, captions, tables, declarations, and upload files.
5. For a manuscript, run `apply_manuscript_profile.py` with explicit role and
   prose-style arguments plus the resolved `--font-name`, `--body-font-size`,
   `--title-font-size`, `--table-font-size`, and `--line-spacing` values.
6. Run `enforce_docx_line_page_numbers.py` on every modified DOCX with the resolved page-number position.
7. Run `python3 "$SKILL_ROOT/scripts/audit_docx_manuscript_style.py" manuscript.numbered.docx --paragraph-separation literal-blank --expected-line-spacing double` on every modified DOCX, replacing only the spacing token with the validated `style_contract` value and passing all prose/non-body styles explicitly.
8. For a manuscript, run `audit_docx_front_matter.py` with the resolved blinded/unblinded mode, front-matter alignment, role arguments, page-number position, body size, and global line-spacing token.
9. For a manuscript, run `audit_docx_semantic_rhythm.py` with the same resolved
   font and size arguments; require identical resolved line spacing across the
   complete manuscript, exact 15/12 pt fallbacks when no official override
   exists, body-sized author/affiliation/Keywords/declaration/reference roles,
   a bold Keywords label, and exact semantic blank-line boundaries.
10. Compare extracted text before and after; any unauthorized text change fails content preservation.
11. Render DOCX with a reliable renderer available in the current host and inspect every page at 100% zoom.
12. Check title/heading color, clipping, overlap, tables, captions, page breaks, orphan headings, figures, headers/footers, visible continuous line numbers, dynamic page numbers, and references.
13. If a mechanical audit reports a repairable failure, correct the generated DOCX automatically; do not ask the user to adjust it in Word.
14. Map every format-plan check ID into `07_format_audit.json`, attach inspected evidence, and mark it `PASS`, `FAIL`, or `NOT_ASSESSABLE`.
15. Validate plan-to-output closure with `validate_journal_format_audit.py`.
16. For a manuscript, combine structural, front-matter, semantic-rhythm, preservation, journal, and render results with `validate_format_release.py`; require `FORMAT_RELEASE_PASS`.
17. Fix and re-render after every layout-sensitive change.

## Submission-package files

Load [submission-package-contract.md](submission-package-contract.md) for cover
letters, response letters, highlights, declarations, review proposals, and
other editable submission text. Do not run the manuscript normalizer or
fabricate front matter. Use the dedicated package normalizer, whole-document
package audit, and package release validator.

Codex may use an installed document/PDF capability. Claude Code may use an
available office converter, renderer, script, or MCP tool. If rendering is
unavailable, disclose that visual QA was not completed and return the format
gate `NOT ASSESSABLE`.

## Output separation

When authorized to revise, normally produce:

- `manuscript_tracked.docx` or another clearly reviewable redline
- `manuscript_clean.docx`
- `revision_log.tsv`
- `07_format_audit.json`
- `07_structural_format_audit.json`
- `07_front_matter_audit.json`
- `07_semantic_rhythm_audit.json`
- `07_format_release.json`

Do not strip comments, tracked changes, citation fields, author identity, or metadata until the journal stage and user's requested deliverable are known.

## Mechanical audit boundary

The style script flags explicit non-black or theme-colored title/heading text,
title/heading shading, decorative paragraph borders, non-zero effective
body-paragraph spacing, missing literal blank separators, multiple blank
separators, missing or restarted section line numbering, suppressed line
numbers, and missing dynamic page fields in active page stories. It also checks
the resolved body and separator line spacing against an explicit multiple
(`single`, `1.15`, `1.5`, `double`) or point rule (`exact:24pt`,
`at-least:14pt`). It inspects top-level body prose and does not treat table-cell
paragraphs as adjacent body paragraphs. It cannot prove compliance with a
journal template or visual correctness. Always combine it with official-source
review and rendered page inspection.

The journal-format plan validator checks that all required rule categories have
a source-linked implementation and verification method. The DOCX style audit
checks only part of that plan, while the front-matter and semantic-rhythm audits
check separate semantic and visual surfaces. `validate_format_release.py` closes the applicable
formatting gates but cannot establish scientific validity, citation validity,
editorial acceptance, or successful submission.
