# Productivity

General workflow skills for planning, handoffs, teaching, grilling, formal logic, and skill-writing discipline.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use user-invoked skills only when explicitly called; most are conversation-control modes.
- Use `grilling` when the model should proactively stress-test a plan or design before work begins.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- [grill-me](./grill-me/SKILL.md) — A relentless interview to sharpen a plan or design.
- [handoff](./handoff/SKILL.md) — Compact the current conversation into a handoff document for another agent to pick up.
- [teach](./teach/SKILL.md) — Teach the user a new skill or concept, within this workspace.
- [writing-great-skills](./writing-great-skills/SKILL.md) — Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Planning and conversation control

- [grilling](./grilling/SKILL.md) — Interview the user relentlessly about a plan or design.

### Reasoning and argumentation

- [to-logic](./to-logic/SKILL.md) — Проверяет и исправляет формальную логику рассуждений, силлогизмов и аргументирующих текстов.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
