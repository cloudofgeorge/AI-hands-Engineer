---
name: insecure-defaults
description: Audit code and deployment configuration for fallback secrets, default credentials, fail-open switches, weak cryptography, permissive access, and debug leakage; trace candidates to reachable security decisions.
---

# Insecure defaults audit

## Portable execution

Follow [the repository portability convention](../../../PORTABILITY.md). Use actual host capabilities and local resource paths. Role names and tool-call examples describe work to perform, not installed agents or APIs. Keep evidence and task status in files when native orchestration is unavailable; report any missing independent review or enforcement.


Audit the requested file, directory, or repository using the local category corpus. A directory explicitly selected by the user remains in scope even if it contains tests or fixtures. Do not silently exclude it.

## Category references

- [Fallback secrets](references/fallback-secrets.md)
- [Default credentials](references/default-credentials.md)
- [Fail-open security](references/fail-open-security.md)
- [Weak cryptography](references/weak-crypto.md)
- [Permissive access](references/permissive-access.md)
- [Debug features](references/debug-features.md)

Each category also has a sibling JSON seed-pattern file. Read both before searching. If a required corpus file is unreadable, report the missing coverage; do not invent substitute rules and claim a complete audit.

## Method

1. Profile the stack, entry points, configuration wrappers, and deployment manifests within the requested scope.
2. Search each category using its seeds and derived patterns for the actual framework, language, wrappers, and manifests. Seeds are a floor, not the whole search. POSIX ERE patterns use `[[:space:]]` and `[0-9]`; do not silently run unsupported `\s`, `\d`, or `\b` patterns with a different grep dialect.
3. Record candidates without declaring them vulnerabilities. Deduplicate by category, file, and line; different categories at the same line remain distinct claims.
4. For each candidate, trace production reachability, the value actually used, the insecure property, and the security decision it reaches. Look for evidence that refutes the claim before confirming it.
5. Distinguish configurable fallback behavior from an unconditional insecure value. Missing environment configuration is irrelevant to an unconditional value. For configurable values, inspect all relevant deployment manifests; partial or unknown coverage does not prove the unsafe fallback unreachable.
6. Report confirmed findings with source/sink/validation citations, impact, and remediation. Preserve refuted candidates and their reasons. Keep incomplete traces as unresolved coverage gaps, not confirmed vulnerabilities or proof of safety.

The categories can be processed sequentially or by available reviewers. Use an independent reviewer for confirmation where possible; disclose when only self-review occurred. No plugin command or workflow API is required.

## Output

Record target revision, scope, category coverage, seed and derived searches, candidates, confirmation/refutation evidence, unresolved gaps, and findings. An empty search or zero confirmed findings is not proof of absence. Fixed syntax-only checks may be better implemented in a linter or Semgrep rule; this skill focuses on context and reachability.
