# Brainstorming

Collaborative design and specification workflows for turning early ideas into implementation-ready plans.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use `brainstorming` before creative implementation work: new features, components, behavior changes, or product/design decisions.
- Do not use for routine documentation-only edits, mechanical repository maintenance, or already-approved implementation plans.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Idea shaping and design gates

- [brainstorming](./brainstorming/SKILL.md) — Use before creative work to explore project context, clarify requirements, compare approaches, present a design, and get approval before implementation.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
