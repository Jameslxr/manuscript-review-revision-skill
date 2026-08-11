# Editable submission-package DOCX contract

Load this reference for cover letters, response letters, highlights,
declarations, review proposals, and other editable submission text that is not
a manuscript with title-page/front-matter semantics.

## Source and content boundary

Apply direct editor instructions, the current exact journal template, and the
current official author guide before this fallback profile. Formatting work
must preserve every text node, hyperlink target, comment, field, tracked
change, figure, and table. The format-only Skill must not add, rewrite, or
paraphrase an AI-use declaration or other declaration.

## Package-wide profile

- Use one explicit line-spacing token throughout the package file. Use the
  exact journal/user value when specified; otherwise use `single` for a
  journal-neutral letter/package file.
- Use Times New Roman 12 pt, black, left-aligned text and 1-inch margins unless
  the current source resolves another value.
- Set every visible body and table-cell paragraph, including empty separators,
  to `spaceBefore=0 pt`, `spaceAfter=0 pt`, with automatic spacing disabled.
- Keep run-level bold and italics. Do not preserve an accidental undersized
  salutation, closing, author, signature, reviewer-comment, or declaration
  style.
- Use real empty Word paragraphs for vertical separation. Do not substitute
  paragraph spacing or manual line breaks.

For a cover letter, resolve the salutation and closing from exact text or pass
their one-based top-level paragraph numbers. Require one empty paragraph after
the salutation, between body paragraphs, before the closing, and between the
closing and first signature paragraph. Keep consecutive signature/address
paragraphs compact. Preserve existing compact sender/recipient blocks before
the salutation, collapse duplicate blank runs, and require one blank immediately
before the salutation when a preamble exists. If salutation or closing is
missing/ambiguous, stop and inventory instead of guessing.

For response letters and generic editable package text, use one real empty
paragraph between adjacent non-list top-level blocks. Keep consecutive list
items compact, with one empty paragraph around the list block. Do not insert
blank paragraphs inside tables.

## Deterministic sequence

```bash
python3 "$SKILL_ROOT/scripts/apply_submission_package_profile.py" input.docx \
  --out package.normalized.docx \
  --artifact-type <cover-letter|response-letter|generic> \
  --line-spacing <resolved-token>

python3 "$SKILL_ROOT/scripts/enforce_docx_line_page_numbers.py" \
  package.normalized.docx --out package.release.docx \
  --page-number-position <resolved-position>

python3 "$SKILL_ROOT/scripts/audit_docx_submission_package.py" \
  package.release.docx \
  --artifact-type <cover-letter|response-letter|generic> \
  --expected-line-spacing <resolved-token> \
  --expected-font-name "Times New Roman" --expected-font-size 12 \
  --expected-margin-inches 1 \
  --output-json package.audit.json

python3 "$SKILL_ROOT/scripts/validate_submission_package_release.py" \
  package.audit.json \
  --content-preservation-status PASS \
  --journal-status <PASS|NOT_APPLICABLE|NOT_ASSESSABLE> \
  --render-status PASS \
  --output-json package.format-release.json
```

Apply explicit `--salutation-paragraph` and `--closing-paragraph` selectors
when text-based cover-letter role resolution is ambiguous. The package audit
includes whole-document font, size, color, alignment, margin, line-spacing,
0/0 spacing, natural blank-boundary, continuous line-number, and dynamic
page-number checks. Only `PACKAGE_FORMAT_RELEASE_PASS` closes this contract.
Render and inspect every page after the last layout-sensitive change.
