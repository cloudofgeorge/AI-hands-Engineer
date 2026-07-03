# UltraSkills

Imported engineering skill bundle for staged research, architecture, execution planning, implementation, code review, workflow-runner orchestration, role lenses, and compact communication modes.

This README is a routing index for agents. Keep it short; detailed procedures belong in each linked `SKILL.md`, role file, or supporting reference.

## Hermes discovery

When this repository's `skills/` directory is installed or configured as a Hermes external skill source, Hermes can discover the nested skills under `skills/engineering/UltraSkills/skills/*/SKILL.md` after a skill reload or new session.

A few imported skills intentionally reuse names that also exist elsewhere in this repository (`forthright`, `grill-me`, `improve-codebase-architecture`). If a Hermes installation exposes only one bare name, use this README or the parent [Engineering README](../README.md) to choose the intended UltraSkills path.

## How to choose

- Use the staged-delivery skills when work needs a durable research → architecture → execution-plan → implementation chain.
- Use `code-review-orchestrator` when the output should merge specialist reviewer perspectives into a single verdict.
- Use `hat` for a temporary role lens; use the workflow skills for task execution.
- Use `docs-writer` for instructional documentation; use `devrel-copywriter` for product-facing README framing.
- Use compression/persona skills (`caveman`, `forthright`, `humanizer`) only when their communication contract is the actual task.

## User-invoked

None currently. The imported UltraSkills `SKILL.md` files in this bundle are model-invoked unless their frontmatter changes.

## Model-invoked

### Staged delivery and review

- [research-critic](./skills/research-critic/SKILL.md) — Produce a reusable pre-implementation research artifact by having a researcher create a canvas and a second reviewer attack the assumptions.
- [create-architecture](./skills/create-architecture/SKILL.md) — Create, improve, align, or audit an architecture decision package, including `ARCHITECTURE.md`, C4/DDD artifacts, migration slices, and colocated context rules.
- [dev-harness](./skills/dev-harness/SKILL.md) — Orchestrate execution planning and delegation after approved research or architecture context exists.
- [implementation-harness](./skills/implementation-harness/SKILL.md) — Execute the approved development stage against closed research and execution-plan contracts without reopening broad discovery.
- [code-review-orchestrator](./skills/code-review-orchestrator/SKILL.md) — Fan out code review across specialist roles and merge must-fix, should-fix, and can-delay findings into a pass/fail verdict.
- [loop](./skills/loop/SKILL.md) — Run repeated task cycles with explicit state, worker handoff, progress reporting, and safe stop conditions.
- [orbita](./skills/orbita/SKILL.md) — Drive workflow-runner host-adapter jobs, follow runner stdout, handle host actions, and continue/resume workflow runs.

### Docs, design, and skill authoring

- [create-design](./skills/create-design/SKILL.md) — Create, rewrite, review, or restructure a project's design-memory system and operational design artifacts.
- [create-skill](./skills/create-skill/SKILL.md) — Create, rewrite, audit, or restructure a Claude/OpenClaw-style skill folder from source material, prompts, SOPs, notes, or an existing skill.
- [docs-writer](./skills/docs-writer/SKILL.md) — Write or rewrite usage, setup, onboarding, migration, API, and reference documentation so readers succeed quickly.
- [devrel-copywriter](./skills/devrel-copywriter/SKILL.md) — Shape repository README framing and opening structure when the README is a product-facing entrypoint.
- [improve-codebase-architecture](./skills/improve-codebase-architecture/SKILL.md) — Legacy donor/reference skill for module, interface, seam, and depth thinking; prefer `create-architecture` for active architecture work.

### Communication, writing, and role lenses

- [caveman](./skills/caveman/SKILL.md) — Use an ultra-compressed communication mode that cuts filler while keeping technical accuracy.
- [forthright](./skills/forthright/SKILL.md) — Apply high-compression internal communication for ACP workers, subagents, agent handoffs, and AI-only operational files.
- [grill-me](./skills/grill-me/SKILL.md) — Relentlessly interview the user about a plan or design until assumptions and branches are resolved.
- [hat](./skills/hat/SKILL.md) — Activate, switch, list, query, or clear a sticky repo-role lens discovered from `roles/*`.
- [humanizer](./skills/humanizer/SKILL.md) — Polish existing text so it sounds natural, casual, clear, or human without changing the core message.
- [cover-letter-writer](./skills/cover-letter-writer/SKILL.md) — Write or rewrite short, high-conviction cover letters, recruiter outreach, warm intros, and hiring-manager messages.

## Supporting directories

| Directory | Purpose |
| --- | --- |
| [`agents/`](./agents/) | Codex/agent role configuration files used by UltraSkills workflows. |
| [`roles/`](./roles/) | Role definitions, rubrics, learnings, and references used by `hat`, review, and staged workflows. |
| [`shared/`](./shared/) | Shared delegation contracts, templates, review contracts, and go-to-market context. |
| [`workflows/`](./workflows/) | Workflow-runner definitions and schemas used by Orbita and related flows. |
| [`scripts/`](./scripts/) | Bundle validation and generation helpers. |

## Maintenance

- Update this README and the parent [Engineering README](../README.md) whenever an UltraSkills skill is added, removed, renamed, or moved.
- Keep every bullet trigger-oriented; put workflow detail in the linked skill or reference file.
- Re-check duplicate `name` values whenever importing a new upstream UltraSkills version.
