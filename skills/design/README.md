# Design

Design, visual prototyping, image generation, and critique skills.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use `impeccable` when the task is design direction, critique, polishing, or taste-making.
- Use `huashu-design` when the deliverable should be a high-fidelity HTML prototype, interactive demo, slide, or animation.
- Use `imagegen` only when the task is actual image generation or image editing.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Design workflows

- [impeccable](./impeccable/SKILL.md) — Use for frontend interface design, redesign, critique, polish, animation, color, and UI quality audits.
- [huashu-design](./huashu-design/SKILL.md) — Use for high-fidelity HTML prototypes, interaction demos, slides, animations, and design expert review with HuaShu design personas.
- [imagegen](./imagegen/SKILL.md) — Use for image generation, image editing, inpainting, masks, background changes, product shots, and concept art.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
