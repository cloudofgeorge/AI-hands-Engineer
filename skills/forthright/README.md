# Forthright

A compact communication-mode skill for internal agent-to-agent work and operational handoffs.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use for ACP workers, subagents, reviewer/implementer coordination, and internal file compression.
- Do not use for polished user-facing replies, safety warnings, or destructive confirmations.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Compression mode

- [forthright](./SKILL.md) — High-compression internal communication mode for ACP workers, subagents, handoffs, and AI-only operational files.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
