# Platform compatibility

## Required host capabilities

The scientific rules in this Skill are platform-independent. A host can run the
complete workflow only when it can:

- load an Agent Skill together with its `references/` and `scripts/`;
- read the supplied manuscript and supporting files without mixing versions;
- inspect current official journal and scholarly sources;
- execute the bundled Python validators;
- create at least five real reviewer tasks with fresh, isolated contexts;
- preserve review reports and the synthesis as separate artifacts.

If a required capability is unavailable, mark the affected gate
`NOT ASSESSABLE`. Do not simulate five reviewers by writing five sections in one
conversation.

## Resolve bundled resources

Before running a bundled script, resolve the absolute directory containing this
`SKILL.md` as `SKILL_ROOT`. Never assume that the user's current working
directory is the installed Skill directory.

- Claude Code exposes the installed directory as `${CLAUDE_SKILL_DIR}`; use
  `SKILL_ROOT="${CLAUDE_SKILL_DIR}"` when a shell variable is needed.
- Codex exposes the selected Skill path through its Skill registry or session
  instructions.
- Other Agent Skills hosts must provide an equivalent installed-resource path.

Use:

```text
python3 "$SKILL_ROOT/scripts/<script-name>.py" <arguments>
```

## Capability mapping

| Need | Codex example | Claude Code example | Required behavior |
|---|---|---|---|
| Independent reviewers | collaboration/subagent delegation | non-fork `Agent` subagents | Fresh context for every reviewer; no earlier review in the task message |
| Current journal sources | Web, browser, or connected scholarly tools | Web search/fetch, browser, or MCP tools | Prefer official sources and record URLs plus access dates |
| Manuscript and PDF reading | document/PDF capabilities when installed | native readers, Bash converters, or MCP tools | Inspect the supplied files; disclose unreadable components |
| DOCX rendering | document renderer and PDF/image inspection | an available office converter, renderer, or MCP tool | Render and inspect every page; otherwise return `NOT ASSESSABLE` |
| Figure work | installed scientific-figure capability | installed skill, script, or MCP tool | Use only when needed and preserve source-data traceability |
| Validation | bundled Python scripts | bundled Python scripts | Run from `SKILL_ROOT`, not from an assumed working directory |

Capability names vary between installations. The behavior and evidence
requirements above are authoritative; the example tool names are not.

## Claude Code notes

- Personal Skills live at `~/.claude/skills/<skill-name>/SKILL.md`.
- Project Skills live at `.claude/skills/<skill-name>/SKILL.md`.
- Invoke this Skill directly with `/manuscript-review-revision`, or let Claude
  load it from the description when the request matches.
- Use normal `Agent` subagents with fresh isolated contexts for reviewer roles.
  Do not use a fork that inherits the parent conversation for an independent
  review seat.
- Record the real Agent task ID in the panel plan when Claude Code exposes it.

Claude Code documentation:

- [Agent Skills](https://code.claude.com/docs/en/slash-commands)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude configuration directories](https://code.claude.com/docs/en/claude-directory)

## Optional platform-specific capabilities

`agents/openai.yaml` supplies Codex-facing interface metadata and may be ignored
by other Agent Skills hosts. Codex-specific document, PDF, Nature, and figure
Skills are optional accelerators rather than requirements. Use an equivalent
capability when available; never silently lower a scientific or release gate
because a named optional Skill is absent.
