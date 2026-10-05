# Productivity

General workflow skills for handoffs, teaching, grilling, questionnaires, clarification, formal logic, and writing for agents.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use user-invoked skills only when explicitly called; most are conversation-control modes.
- Use `grilling` when the user wants to stress-test a plan, decision, or idea; use `to-questionnaire` when the answers must come from someone else.
- Use `wait-what` to ask for a clearer explanation of the last message.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- [grill-me](./grill-me/SKILL.md) — A relentless interview to sharpen a plan or design.
- [continuity](./continuity/SKILL.md) — Create a compact continuity brief so a fresh agent or session can resume the work.
- [teach](./teach/SKILL.md) — Teach the user a new skill or concept, within this workspace.
- [to-questionnaire](./to-questionnaire/SKILL.md) — Turn decisions or facts the user cannot resolve alone into a Markdown questionnaire for another person.
- [wait-what](./wait-what/SKILL.md) — Re-explain the last message with context, simplified technical English, and the project glossary.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Planning and conversation control

- [grilling](./grilling/SKILL.md) — Stress-test a plan, decision, or idea through a focused interview when the user asks to be grilled.

### Reasoning and argumentation

- [to-logic](./to-logic/SKILL.md) — Проверяет и исправляет формальную логику рассуждений, силлогизмов и аргументирующих текстов.

### Writing for agents

- [writing-for-agents](./writing-for-agents/SKILL.md) — Write or edit agent-facing documents, including skills, `AGENTS.md`, and `CLAUDE.md`, with clear context pointers and focused references.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
