# Editable submission-package DOCX contract

Load this reference for cover letters, response letters, highlights,
declarations, review proposals, and other editable submission text that is not
a manuscript with title-page/front-matter semantics.

Apply direct editor instructions, the current exact journal template, and the
current official author guide before the journal-neutral fallback. Formatting
must preserve text and fields. Use one explicit line-spacing token throughout
the package file (`single` fallback), Times New Roman 12 pt, black,
left-aligned text, 1-inch margins, `spaceBefore=0 pt`, `spaceAfter=0 pt`, and
real empty Word paragraphs unless a current source resolves another token.

For a cover letter, resolve salutation and closing from text or explicit
one-based paragraph numbers. Require one empty paragraph after the salutation,
between body paragraphs, before the closing, and before the first signature
paragraph; keep consecutive signature/address paragraphs compact. For response
letters and generic package text, use one empty paragraph between adjacent
non-list blocks and keep consecutive list items compact. Stop rather than guess
when cover-letter roles are ambiguous.

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
  --output-json package.audit.json

python3 "$SKILL_ROOT/scripts/validate_submission_package_release.py" \
  package.audit.json --content-preservation-status PASS \
  --journal-status <PASS|NOT_APPLICABLE|NOT_ASSESSABLE> \
  --render-status PASS --output-json package.format-release.json
```

The package audit covers all visible body and table-cell paragraphs, including
salutation, body, closing, signature, comments, responses, declarations, and
empty separators. It checks font, size, color, alignment, margins, global line
spacing, 0/0 spacing, semantic blank boundaries, continuous line numbering, and
dynamic page numbering. Only `PACKAGE_FORMAT_RELEASE_PASS` closes the package
contract. Render and inspect every page after the final change.
