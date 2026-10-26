---
name: c-review
description: Review native C/C++ userspace code for memory safety, arithmetic, lifecycle, concurrency, and platform security defects, with explicit coverage and source evidence.
---

# C/C++ security review

## Portable execution

Follow [the repository portability convention](../../../../../PORTABILITY.md). Use actual host capabilities and local resource paths. Role names and tool-call examples describe work to perform, not installed agents or APIs. Keep evidence and task status in files when native orchestration is unavailable; report any missing independent review or enforcement.


Review source by location, then sweep relevant bug classes that the location pass did not cover. Use for native userspace applications and services. Kernel, bare-metal, and managed-runtime analysis require different domain assumptions.

## Scope and preparation

Establish the finding scope, allowed context scope, attacker model (`REMOTE`, `LOCAL_UNPRIVILEGED`, or `BOTH`), and requested severity filter from the user's task. Ask only where ambiguity changes the audit. Keep the source snapshot stable and record its revision. Wider caller/build context may inform reachability without expanding the finding scope.

Resolve this package from the loaded file: scripts and references are two directories above this `SKILL.md`. Use Python/`uv` and the dependencies declared in [the script project](../../scripts/pyproject.toml) when running the deterministic helpers. There is no plugin cache or workflow service to locate.

## Review method

1. **Enumerate.** Use [enumerate_units.py](../../scripts/enumerate_units.py) to partition source into bounded units and write assignments. Run its `--help` for flags; provide `--root` and `--out-dir`, and record exclusions. Each unit needs an owner, including cold error paths. If enumeration is unavailable, record a manual inventory and label coverage as unmeasured by the automated gate.
2. **Establish context.** Determine actual C/C++, POSIX, and Windows API usage, entry points, shared-state structures, and attacker reachability. A platform header alone is insufficient evidence for platform gating.
3. **Read by location.** For each unit check bounds at writes, integer width/signedness/wrap, allocation and release, `sizeof` arithmetic, NUL termination, return values, caller contracts, banned APIs with attacker-controlled data flow, initialization, and macro contracts. Follow callers and callees. Account for every applicable site even after finding one bug.
4. **Keep evidence.** Record unit/question/site evidence and findings in separate part files. Retain the [artifact schema reference](../../references/artifact-schemas.md) when using the assembler. Use the [reviewer checklist](../../references/roles/c-review-worker.md) for source review. Reviewers should modify only their assigned output; file permissions require actual host enforcement, not a promise in a prompt.
5. **Sweep gaps.** Use the [56-class reference](../../references/bug-classes.md) for applicable classes without evidence from the location pass. Distinguish searched-with-no-finding, not searched, and excluded-by-scope. For a requested shared-state audit, enumerate fields, invariants, all writers, and all readers.
6. **Merge and validate.** For compatible part artifacts, use [assemble_findings.py](../../scripts/assemble_findings.py) and [check_ledger.py](../../scripts/check_ledger.py). Read their `--help` and validate actual formats before invoking. Supply the expected part names/counts and `--no-judge` unless a real independent adjudication occurred. Never fabricate counts or ledger rows to make a gate pass.
7. **Report.** Provide findings, evidence, impact, remediation, reviewed scope, omissions, failures, and artifact paths. A completed file is not proof that the coverage gate accepted it. Report checks satisfied versus checks required, not merely questions answered. Without compatible gate artifacts, state coverage as unmeasured.

## Review independence and limitations

Process bounded units sequentially or use available reviewers. A sequential review keeps the method but does not reproduce the original plugin's tool restrictions, scheduling, or measured performance. A prompt cannot prevent a reviewer from reading or changing evidence; use an immutable source snapshot or real host permissions when isolation matters.

The coverage checker detects some omissions and inconsistent records. It is not a tamper-proof proof of correctness and can miss count-preserving source changes. No false-positive judge runs automatically: label findings and severities as reviewer assessments until an independent validation actually occurs. Preserve failed and incomplete work rather than reporting zero findings as a clean audit.
