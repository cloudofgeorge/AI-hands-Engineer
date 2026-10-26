# regression-hunt

Portable adaptation of Trail of Bits guidance. Read the selected skill by path and keep its references and reusable helpers together. Native plugin manifests, commands, hooks, UI metadata, runtime orchestration, and plugin-only evaluation harnesses have been removed. The analysis methods and supporting material are retained; this version does not inherit the original plugin runtime or benchmark guarantees.

## Skills

- [adjudicate-regression](./skills/adjudicate-regression/SKILL.md) — Use when deciding whether source and live reproduction evidence establish a new regression or an exclusion.
- [hunt-regressions](./skills/hunt-regressions/SKILL.md) — Use when discovering possible regressions from a pinned change and its callers before reproduction.
- [prepare-regression](./skills/prepare-regression/SKILL.md) — Use when pinning before/after sources and collecting PR or commit context for a regression investigation.
- [regression-hunt](./skills/regression-hunt/SKILL.md) — Use when investigating regressions in PRs or commits, coordinating a regression campaign, or resuming saved progress.
- [replay-regression](./skills/replay-regression/SKILL.md) — Use when independently verifying a supplied PoC against fresh live before/after deployments.
- [report-regressions](./skills/report-regressions/SKILL.md) — Use when assembling or refreshing an evidence-linked regression report from saved campaign decisions.
- [reproduce-regression](./skills/reproduce-regression/SKILL.md) — Use when deploying before/after systems and building a live-system PoC for a regression candidate.

## References

[references/](./references/) contains supporting material. Load only the files needed by the selected skill.

## Scripts

[scripts/](./scripts/) contains supporting material. Load only the files needed by the selected skill.

## Docs

[docs/](./docs/) contains supporting material. Load only the files needed by the selected skill.

## Attribution and use

Derived from [Trail of Bits skills](https://github.com/trailofbits/skills). Local portability adaptations made on 26 October 2026. Retain the [CC BY-SA 4.0 license](../LICENSE) when copying this material. Use the current host's real permissions and capabilities; prompts do not enforce isolation.
