---
name: rust-review
description: Review Rust code for unsafe and FFI invariants, concurrency, async cancellation, arithmetic, filesystem, and trust-boundary defects with per-pass coverage and evidence-backed findings.
---

# Rust security review

## Portable execution

Follow [the repository portability convention](../../../../../PORTABILITY.md). Use actual host capabilities and local resource paths. Role names and tool-call examples describe work to perform, not installed agents or APIs. Keep evidence and task status in files when native orchestration is unavailable; report any missing independent review or enforcement.


Use the bundled domain prompts and deterministic planning/report helpers. This skill requires no registered agent types, native task ledger, or host-specific scheduler.

## Prepare

Establish the finding scope, allowed caller/build context, attacker model, severity filter, and source revision. Resolve this package two directories above the loaded `SKILL.md`; do not search host caches. Confirm Rust source exists and locate the Cargo manifest. Use the current host's model by default.

Record actual capability flags: unsafe code, FFI, concurrency, async, packed representation, and filesystem I/O. Search with a regex dialect that supports the patterns; use ripgrep or translate patterns explicitly for POSIX grep. An unsupported regex returning no matches is not evidence that a capability is absent.

## Plan and review

1. Create an output directory with `context.md`, `findings/`, and `coverage/`. Describe purpose, scope, entry points, trust boundaries, hardening, manifest location, and capability flags.
2. Inspect [build_run_plan.py](../../scripts/build_run_plan.py) with `--help` and generate a plan from [the cluster manifest](../../prompts/clusters/manifest.json). Its historical `--plugin-root` flag simply takes this package directory; it does not require a plugin installation. Keep all selected prompt files and explicit skipped-pass reasons.
3. Process each generated worker prompt as a bounded review task, sequentially or through available reviewers. Read [the worker protocol](../../references/roles/rust-review-worker.md) for finding and coverage formats. Track pending/completed/failed attempts in a file rather than a native task API. No cache-primer task or prescribed concurrency is required.
4. Read the source, callers, callees, macro expansions and configuration relevant to each pass. An `unsafe` block alone is not a finding. Trace violated preconditions, attacker control, missing enforcement, and impact; retain source citations and counterevidence.
5. Validate every worker's artifacts with [validate_artifacts.py](../../scripts/validate_artifacts.py). Distinguish a completed clear pass from a failed or missing output. Retry only bounded failures that can make progress; list the remaining coverage gaps.
6. Deduplicate findings using [the dedup procedure](../../references/roles/rust-review-dedup-judge.md), then verify reachability and severity using [the false-positive procedure](../../references/roles/rust-review-fp-judge.md). Use independent reviewers when available. A same-agent re-read is self-review, so label it and do not claim independent confirmation.
7. Use [generate_sarif.py](../../scripts/generate_sarif.py) for supported artifact formats. Report findings, confidence, severity evidence, source revision, exclusions, skipped passes, failed tasks, and output paths. Missing adjudication must not be silently converted into an accepted verdict.

## Constraints

Keep source and output paths separate. Audit scope and context scope are distinct: reading a caller elsewhere does not authorize unrelated findings or changes. Preserve raw findings and changes made during deduplication/adjudication. Tool names in retained role examples describe capabilities; they neither grant tools nor constrain them. No reviewer isolation is guaranteed unless the host actually enforces it.

The original host's cache, scheduling, and agent permissions are absent. This adaptation preserves the analysis method and artifact checks, not its benchmark or performance guarantees.
