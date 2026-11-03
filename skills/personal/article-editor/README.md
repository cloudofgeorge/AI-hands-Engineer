# Article Editor

`article-editor` helps write, rewrite, and shorten explanatory, workplace, and analytical articles. It prioritizes logic and accuracy, followed by clarity and brevity.

## Usage

Load the entire skill directory, including `references/`, through your agent's skill mechanism. You can also provide [SKILL.md](./SKILL.md) directly while keeping its supporting files accessible. Automatic selection depends on the environment; name the skill in your prompt to invoke it explicitly.

Example:

> Use article-editor. Edit the article below for new employees: check the logic, explain necessary terms, and remove repetition. Preserve conditions and exceptions. Show the finished text.

For a new article, provide the topic, audience, purpose, and source material. Specify any requirements for length, tone, or outline approval separately.

## Result

By default, the agent delivers a finished article without internal checklists. When source materials contradict each other, it asks which source is current or explicitly marks the text as incomplete rather than choosing a convenient version.

The skill does not impose a fixed paragraph length or require shortening by a fixed percentage. It is not intended for creative fiction or requests to fix typos only. To verify external facts, the agent needs access to the relevant sources.

The existing [edit-article](../edit-article/SKILL.md) remains a separate option with section approval and paragraph-length limits. For routine work on an article's logic and clarity, choose `article-editor`.

## Files

- [SKILL.md](./SKILL.md) — instructions for the agent.
- [Examples](./references/examples.md) — before-and-after editing decisions.
- [Rationale and validation](./references/validation.md) — method sources and skill maintenance guidance.
