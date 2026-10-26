# post-patch-validation

Portable adaptation of Trail of Bits guidance. Read the selected skill by path and keep its references and reusable helpers together. Native plugin manifests, commands, hooks, UI metadata, runtime orchestration, and plugin-only evaluation harnesses have been removed. The analysis methods and supporting material are retained; this version does not inherit the original plugin runtime or benchmark guarantees.

## Skills

- [post-patch-validation](./skills/post-patch-validation/SKILL.md) — Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. Use after a patch exists and before accepting, merging, or reporting it as fixed; also use when an AI-generated patch, remediation commit, pull request, or proposed upstream fix needs adversarial post-patch validation across any language.

## Attribution and use

Derived from [Trail of Bits skills](https://github.com/trailofbits/skills). Local portability adaptations made on 26 October 2026. Retain the [CC BY-SA 4.0 license](../LICENSE) when copying this material. Use the current host's real permissions and capabilities; prompts do not enforce isolation.
