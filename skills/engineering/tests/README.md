# Testing and validation skills

Six Trail of Bits packages containing **26 skills**, imported from [trailofbits/skills](https://github.com/trailofbits/skills) at commit [`196a9073ab10d35bacf111f945e02c00b2c6883a`](https://github.com/trailofbits/skills/tree/196a9073ab10d35bacf111f945e02c00b2c6883a) on 26 October 2026.

The analysis methods, shared references, role prompts, templates, and reusable scripts are retained. Host-specific plugin packaging, runtime workflows, UI metadata, and plugin evaluation harnesses have been removed; dependent instructions are adapted for portable execution. Trail of Bits and upstream contributors retain attribution; the included [CC BY-SA 4.0 license](./LICENSE) accompanies these imported materials. This routing README is a local addition.

## Choose a package

| Package | Skills | Use when | Entry point |
| --- | ---: | --- | --- |
| Property-based testing | 1 | Writing invariants, reviewing property tests, or interpreting minimized failures. | [property-based-testing](./property-based-testing/skills/property-based-testing/SKILL.md) |
| Mutation testing | 1 | Configuring campaigns or examining mutations that tests did not catch. | [mutation-testing](./mutation-testing/skills/mutation-testing/SKILL.md) |
| Testing Handbook | 15 | Fuzzing, sanitizers, coverage, timing behavior, and cryptographic test vectors. | Choose a skill below; [upstream overview](./testing-handbook-skills/README.md). |
| Regression hunt | 7 | Investigating changes through pinned evidence and independent reproduction. | [regression-hunt](./regression-hunt/skills/regression-hunt/SKILL.md) |
| Post-patch validation | 1 | Testing a security patch against its baseline, variants, and regressions. | [post-patch-validation](./post-patch-validation/skills/post-patch-validation/SKILL.md) |
| Spec-to-code compliance | 1 | Checking implementation against documented requirements. | [spec-to-code-compliance](./spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md) |

## Invocation

All 26 manifests are model-invoked: none sets `disable-model-invocation: true`. Select the narrowest matching skill, and retain its supporting package files.

For direct use in this repository:

```text
Read skills/engineering/tests/property-based-testing/skills/property-based-testing/SKILL.md
and use it to review the properties tested by this suite.
```

These source copies are available by file path immediately. Hosts configured to discover this repository's nested skills can pick them up on refresh or the next session. Other hosts need their own skill-directory configuration. Read skills directly by path; no plugin commands are registered.

## Testing Handbook skills

| Skill | Use when |
| --- | --- |
| [address-sanitizer](./testing-handbook-skills/skills/address-sanitizer/SKILL.md) | Detecting memory errors with sanitizer builds. |
| [aflpp](./testing-handbook-skills/skills/aflpp/SKILL.md) | Running AFL++ fuzzing campaigns. |
| [atheris](./testing-handbook-skills/skills/atheris/SKILL.md) | Fuzzing Python and native Python extensions. |
| [cargo-fuzz](./testing-handbook-skills/skills/cargo-fuzz/SKILL.md) | Fuzzing Rust crates. |
| [constant-time-testing](./testing-handbook-skills/skills/constant-time-testing/SKILL.md) | Measuring cryptographic timing behavior. |
| [coverage-analysis](./testing-handbook-skills/skills/coverage-analysis/SKILL.md) | Measuring which code a fuzzing campaign reaches. |
| [fuzzing-dictionary](./testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md) | Supplying tokens and magic values to fuzzers. |
| [fuzzing-obstacles](./testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md) | Investigating checks and state that block fuzzing. |
| [harness-writing](./testing-handbook-skills/skills/harness-writing/SKILL.md) | Designing and improving fuzzing entry points. |
| [libafl](./testing-handbook-skills/skills/libafl/SKILL.md) | Building custom fuzzers with LibAFL. |
| [libfuzzer](./testing-handbook-skills/skills/libfuzzer/SKILL.md) | Fuzzing C/C++ targets with LLVM libFuzzer. |
| [ossfuzz](./testing-handbook-skills/skills/ossfuzz/SKILL.md) | Preparing continuous fuzzing through OSS-Fuzz. |
| [ruzzy](./testing-handbook-skills/skills/ruzzy/SKILL.md) | Fuzzing Ruby and native Ruby extensions. |
| [testing-handbook-generator](./testing-handbook-skills/skills/testing-handbook-generator/SKILL.md) | Creating or refreshing skills from Handbook content. |
| [wycheproof](./testing-handbook-skills/skills/wycheproof/SKILL.md) | Checking cryptographic implementations against test vectors. |

## Regression hunt stages

The [coordinator](./regression-hunt/skills/regression-hunt/SKILL.md) selects these stages; they can also be addressed individually when their inputs exist:

- [prepare-regression](./regression-hunt/skills/prepare-regression/SKILL.md) — Pin source revisions and change context.
- [hunt-regressions](./regression-hunt/skills/hunt-regressions/SKILL.md) — Identify reachable regression candidates.
- [reproduce-regression](./regression-hunt/skills/reproduce-regression/SKILL.md) — Execute a proof of concept against both states.
- [replay-regression](./regression-hunt/skills/replay-regression/SKILL.md) — Independently repeat the reproduction.
- [adjudicate-regression](./regression-hunt/skills/adjudicate-regression/SKILL.md) — Assess whether the evidence establishes a regression.
- [report-regressions](./regression-hunt/skills/report-regressions/SKILL.md) — Produce reports from saved decisions.

## Runtime and portability

Keep each skill's supporting package files intact. Regression skills reference shared scripts and documentation, so flattening the folders breaks their resource paths.

- The Handbook is a collection of 15 skills; select the relevant entry above.
- Property testing, mutation campaigns, and fuzzing require their language-specific tools.
- Regression Hunt helpers require Python 3.13+, `uv`, appropriate Git support, and POSIX locks. Independent reproduction remains an evidence requirement; if unavailable, report that limitation.
- Post-patch validation uses its local Python runner. Specification compliance now follows a file-based requirement analysis and review procedure.
- No runtime workflow, native agent registration, or hook is installed. Role prompts and tool names describe capabilities; use [the portability convention](../../PORTABILITY.md).

These are local adaptations of the source packages. Packaging checks do not establish behavioral equivalence to the original plugin runtime.
