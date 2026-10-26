# Security engineering

Choose a narrow skill for the task. This section contains three existing security skills and **14 Trail of Bits groups with 26 skill manifests**.

## Existing skills

- [security-best-practices](./security-best-practices/SKILL.md) — Language and framework security reviews.
- [security-threat-model](./security-threat-model/SKILL.md) — Repository-grounded trust boundaries and abuse paths.
- [security-ownership-map](./security-ownership-map/SKILL.md) — Sensitive-code ownership and bus-factor analysis.

## Trail of Bits packages

Imported from [trailofbits/skills](https://github.com/trailofbits/skills/tree/196a9073ab10d35bacf111f945e02c00b2c6883a) on 26 October 2026. Adapted locally to retain skill methods, references, role prompts, and reusable scripts while removing host-specific packaging and runtime orchestration. Attribution belongs to Trail of Bits and upstream contributors; the imported files are accompanied by their [CC BY-SA 4.0 license](./LICENSE-trailofbits). This routing README is a local addition.

| Package | Skill manifests | Use when |
| --- | ---: | --- |
| [audit-context-building](./audit-context-building/skills/audit-context-building/SKILL.md) | 1 | Understand architecture, data flow, and invariants before auditing. |
| [differential-review](./differential-review/skills/differential-review/SKILL.md) | 1 | Review changes for security impact and regressions. |
| [static-analysis](./static-analysis/README.md) | 3 | Run CodeQL or Semgrep and process SARIF results. |
| [variant-analysis](./variant-analysis/skills/variant-analysis/SKILL.md) | 1 | Find related instances of a known vulnerability pattern. |
| [fp-check](./fp-check/skills/fp-check/SKILL.md) | 1 | Validate suspected findings and eliminate false positives. |
| [insecure-defaults](./insecure-defaults/SKILL.md) | 1 | Audit fallback secrets, default credentials, fail-open behavior, and unsafe configuration. |
| [sharp-edges](./sharp-edges/skills/sharp-edges/SKILL.md) | 1 | Identify APIs and configuration that invite security mistakes. |
| [supply-chain-risk-auditor](./supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md) | 1 | Assess dependency exposure and maintenance risks. |
| [agentic-actions-auditor](./agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md) | 1 | Review AI agent integrations in GitHub Actions. |
| [semgrep-rule-creator](./semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md) | 1 | Develop and test custom Semgrep rules. |
| [c-review](./c-review/skills/c-review/SKILL.md) | 1 | Run the C/C++ security review workflow. |
| [rust-review](./rust-review/skills/rust-review/SKILL.md) | 1 | Review Rust security boundaries and unsafe code. |
| [constant-time-analysis](./constant-time-analysis/skills/constant-time-analysis/SKILL.md) | 1 | Investigate secret-dependent timing behavior. |
| [building-secure-contracts](./building-secure-contracts/README.md) | 11 | Prepare and assess smart-contract security across supported chains. |

## Individual skills inside bundles

- [algorand-vulnerability-scanner](./building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md)
- [audit-prep-assistant](./building-secure-contracts/skills/audit-prep-assistant/SKILL.md)
- [cairo-vulnerability-scanner](./building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md)
- [code-maturity-assessor](./building-secure-contracts/skills/code-maturity-assessor/SKILL.md)
- [cosmos-vulnerability-scanner](./building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md)
- [guidelines-advisor](./building-secure-contracts/skills/guidelines-advisor/SKILL.md)
- [secure-workflow-guide](./building-secure-contracts/skills/secure-workflow-guide/SKILL.md)
- [solana-vulnerability-scanner](./building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md)
- [substrate-vulnerability-scanner](./building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md)
- [token-integration-analyzer](./building-secure-contracts/skills/token-integration-analyzer/SKILL.md)
- [ton-vulnerability-scanner](./building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md)
- [codeql](./static-analysis/skills/codeql/SKILL.md)
- [sarif-parsing](./static-analysis/skills/sarif-parsing/SKILL.md)
- [semgrep](./static-analysis/skills/semgrep/SKILL.md)

## Invocation and portability

The 26 adapted manifests are model- or user-reachable when discovered by a compatible host. Read the chosen `SKILL.md` directly. `insecure-defaults` is now an ordinary skill.

Audit-context building, specification checks, C/C++ review, Rust review, and insecure-defaults auditing use portable, file-based procedures. Static analysis and post-patch validation use their existing local helpers. The false-positive completion hook is now an explicit checklist. Role prompts can support sequential work or available independent reviewers; missing independence or isolation must be reported.

Follow [the portability convention](../../PORTABILITY.md). Keep supporting resources and licenses with copied skills. Domain tools and target-language dependencies may still be required. These are local adaptations, not byte-identical upstream packages, and the original plugin's runtime guarantees do not apply.
