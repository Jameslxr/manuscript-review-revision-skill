# Generated DOCX release coverage

Use this contract after the final content or layout change in any integrated
`manuscript-review-revision` lane that creates or modifies editable Word files.

## Coverage rule

Place final deliverables and their audit JSON files in a dedicated delivery
root. Keep source files and intermediate DOCX files outside that root. Run the
embedded manuscript or submission-package normalizer and its full release gate
separately for every final DOCX, including tracked and clean copies.

Create one receipt entry per DOCX found recursively in the delivery root:

```json
{
  "schema_version": "1.0",
  "artifacts": [
    {
      "path": "revision/manuscript_clean.docx",
      "sha256": "<sha256 of the final DOCX>",
      "profile": "manuscript",
      "normalizer": "apply_manuscript_profile.py",
      "release_report": "revision/manuscript_clean.format-release.json"
    },
    {
      "path": "submission/cover_letter.docx",
      "sha256": "<sha256 of the final DOCX>",
      "profile": "submission-package",
      "normalizer": "apply_submission_package_profile.py",
      "release_report": "submission/cover_letter.format-release.json"
    }
  ]
}
```

Use `profile: manuscript` only with `apply_manuscript_profile.py` and a release
report whose terminal status is `FORMAT_RELEASE_PASS`. Use
`profile: submission-package` only with
`apply_submission_package_profile.py` and
`PACKAGE_FORMAT_RELEASE_PASS`. The referenced report must retain every required
gate and may use `NOT_APPLICABLE` only for the journal gate.

Run:

```bash
python3 "$SKILL_ROOT/scripts/validate_generated_docx_release.py" \
  <delivery-root> <delivery-root>/07_generated_docx_release_receipt.json \
  --output-json <delivery-root>/07_generated_docx_release.json
```

The validator scans the delivery root, requires exact receipt coverage, checks
each current file hash, parses the referenced release report, and returns
`GENERATED_DOCX_RELEASE_PASS` only when all delivered DOCX files close. Any
post-pass DOCX write invalidates the receipt and requires formatting, audit,
rendering, release composition, hashing, and coverage validation again.

## Non-DOCX files

Do not claim that JSON, TSV, Markdown, figures, data files, or native PDFs have
undergone DOCX formatting. Validate them with their format-specific gates. A PDF
derived from a DOCX may be delivered only from the final hash-closed DOCX and
after rendered-page inspection.
