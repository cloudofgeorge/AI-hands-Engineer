# rust-review

Portable adaptation of Trail of Bits guidance. Read the selected skill by path and keep its references and reusable helpers together. Native plugin manifests, commands, hooks, UI metadata, runtime orchestration, and plugin-only evaluation harnesses have been removed. The analysis methods and supporting material are retained; this version does not inherit the original plugin runtime or benchmark guarantees.

## Skills

- [rust-review](./skills/rust-review/SKILL.md) — Review Rust code for unsafe and FFI invariants, concurrency, async cancellation, arithmetic, filesystem, and trust-boundary defects with per-pass coverage and evidence-backed findings.

## References

[references/](./references/) contains supporting material. Load only the files needed by the selected skill.

## Scripts

[scripts/](./scripts/) contains supporting material. Load only the files needed by the selected skill.

## Prompts

[prompts/](./prompts/) contains supporting material. Load only the files needed by the selected skill.

## Attribution and use

Derived from [Trail of Bits skills](https://github.com/trailofbits/skills). Local portability adaptations made on 26 October 2026. Retain the [CC BY-SA 4.0 license](../LICENSE-trailofbits) when copying this material. Use the current host's real permissions and capabilities; prompts do not enforce isolation.
