# Validation

This document records the reproducible checks for the
`manuscript-review-revision` skill.

## Automated tests

Install the single Python dependency:

```bash
python3 -m pip install -r requirements.txt
```

Run the validator test suite from the repository root:

```bash
python3 -m unittest discover \
  -s manuscript-review-revision/tests \
  -v
```

The current suite contains six representative tests covering:

1. a complete journal profile passes;
2. a journal profile with an unresolved mandatory rule fails;
3. a five-agent independent panel passes;
4. direct citation support passes only with full evidence;
5. metadata-only evidence cannot be labeled direct support;
6. blue or otherwise non-black manuscript headings fail the DOCX style audit,
   while a plain black manuscript passes.

## Syntax checks

```bash
python3 -m py_compile manuscript-review-revision/scripts/*.py
```

## Manual forward test

The initial release was also exercised with a synthetic hepatocellular
carcinoma manuscript targeting a high-tier hepatology journal.

Expected behavior:

- the target journal is fixed before full review;
- six independent functional reviewer roles are selected for the journal tier;
- the panel validator accepts the completed panel;
- the synthesis reports major scientific rework when warranted;
- manuscript revision does not begin before explicit author authorization.

The synthetic manuscript and generated reviews are not distributed because
they are workflow test fixtures rather than reusable Skill resources.

## Validation boundary

These checks validate the Skill structure and selected fail-closed controls.
They do not prove that every scientific judgment is correct, that every journal
website is reachable, or that a submitted manuscript will be accepted.
