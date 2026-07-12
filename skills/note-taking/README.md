# Note-taking

Durable knowledge workspace skills: maintaining a Second Brain across sessions and working with notes in the Obsidian vault.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Use `using-second-brain` for cross-session retrieval, capture, review, handoff, and workspace setup.
- Use `obsidian` for direct filesystem work inside the Obsidian vault: reading, searching, creating, editing, and linking notes.
- When a task needs durable context, start with `using-second-brain` to retrieve and preserve, then use `obsidian` for vault-level edits.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Knowledge workspace

- [using-second-brain](./using-second-brain/SKILL.md) — Retrieve prior context, continue projects, capture research or decisions, prepare handoffs, review knowledge, or set up a Second Brain across sessions and collaborators.
- [obsidian](./obsidian/SKILL.md) — Read, search, create, and edit notes in the Obsidian vault using a filesystem-first workflow.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
