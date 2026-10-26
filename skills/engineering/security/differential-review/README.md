# differential-review

Portable adaptation of Trail of Bits guidance. Read the selected skill by path and keep its references and reusable helpers together. Native plugin manifests, commands, hooks, UI metadata, runtime orchestration, and plugin-only evaluation harnesses have been removed. The analysis methods and supporting material are retained; this version does not inherit the original plugin runtime or benchmark guarantees.

## Skills

- [differential-review](./skills/differential-review/SKILL.md) — Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by counting callers, checks test coverage of modified code, and generates a markdown report. Use when reviewing a PR, commit, or diff for security vulnerabilities, checking whether a change re-introduces a previously fixed bug, asking what else a change could break, or finding which modified code has no test covering it.

## References

[references/](./references/) contains supporting material. Load only the files needed by the selected skill.

## Attribution and use

Derived from [Trail of Bits skills](https://github.com/trailofbits/skills). Local portability adaptations made on 26 October 2026. Retain the [CC BY-SA 4.0 license](../LICENSE-trailofbits) when copying this material. Use the current host's real permissions and capabilities; prompts do not enforce isolation.
