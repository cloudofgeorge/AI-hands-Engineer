# Note-taking

Durable knowledge workspace skills: maintaining a Second Brain across sessions and working with notes in the Obsidian vault.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Use `using-second-brain` to retrieve durable context, capture and develop notes, reuse knowledge in outputs, review, hand off, or set up a knowledge workspace.
- Use `obsidian` for direct filesystem work inside the Obsidian vault: reading, searching, creating, editing, and linking notes.
- When a task needs durable context, start with `using-second-brain` to retrieve and preserve, then use `obsidian` for vault-level edits.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Knowledge workspace

- [using-second-brain](./using-second-brain/SKILL.md) — Retrieve context, capture and connect ideas, turn stored knowledge into outputs, preserve research and decisions, review, hand off, or set up a Second Brain.
- [obsidian](./obsidian/SKILL.md) — Read, search, create, and edit notes in the Obsidian vault using a filesystem-first workflow.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
