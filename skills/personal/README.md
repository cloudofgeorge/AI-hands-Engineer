# Personal

Article writing and editing, personal notes, and cookbook workflows.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`.

## How to choose

- Prefer the narrowest skill that directly matches the task.
- Load additional skills only when their workflow is needed, not just because the topic is adjacent.
- Use `article-editor` for writing or editing reader-facing articles with logic checks and meaning-preserving cuts; it does not require a personal setup.
- Use `edit-article` when the user wants its section-by-section approval workflow and short-paragraph format; do not combine its paragraph limit with `article-editor` by default.
- Use the notes and cookbook skills when the task touches the user’s personal setup.

## User-invoked

Reachable only when you type them (`disable-model-invocation: true`).

- None in this section.

## Model-invoked

Model- or user-reachable; descriptions are trigger-oriented so an agent can route to them automatically.

### Personal workflows

- [article-editor](./article-editor/SKILL.md) — Write, rewrite, or shorten explanatory articles while checking logic, preserving necessary conditions, and removing repetition.
- [edit-article](./edit-article/SKILL.md) — Edit and improve articles by restructuring sections, improving clarity, and tightening prose.
- [obsidian-vault](./obsidian-vault/SKILL.md) — Search, create, and manage notes in the Obsidian vault with wikilinks and index notes.
- [recipe-to-cookbook](./recipe-to-cookbook/SKILL.md) — Turns YouTube cooking videos, Shorts, written recipes, or ingredient lists into a structured cookbook-style recipe in Russian.

## Maintenance

- Update this README whenever a skill is added, removed, renamed, or moved in this section.
- Keep each bullet to one routing sentence: what task should make an agent open that skill.
- Keep `User-invoked` and `Model-invoked` aligned with the `disable-model-invocation` flag in `SKILL.md` frontmatter.
