# Assessment: `ahmedasmar/devops-claude-skills`

**Question:** can these DevOps skills be adopted under `AI-hands/skills/engineering` without a Claude dependency and made agent-agnostic?

**Verdict:** **yes, but rewrite/adapt them rather than vendoring the repository.** The procedural content, scripts, templates, and references are mostly portable Markdown/Python/YAML. Claude-specific coupling is primarily the marketplace/plugin wrapper, plus a few prose references. Before adoption, the skills need safety gates, current-version verification, Linux-portable command fixes, provenance/licensing clarification, and routing integration.

## Sources and scope

- Upstream revision inspected: [`1489c33`](https://github.com/ahmedasmar/devops-claude-skills/tree/1489c33ad8829a11219e423327d6b59f8339cee4), dated 2026-04-11.
- Upstream catalog: [`README.md`](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/README.md).
- AI-hands routing and repository conventions: [`skills/engineering/README.md`](../../README.md) and [`README.md`](../../../../README.md).
- The upstream README claims MIT, but this revision has no tracked `LICENSE`, `NOTICE`, or `COPYING` file. Treat its license as **unverified** until the author supplies the actual MIT license text or clarifies the grant. Do not copy files verbatim meanwhile.

## Upstream inventory and fit

| Upstream skill | Portability | AI-hands destination | Decision |
| --- | --- | --- | --- |
| `iac-terraform` | High | `skills/engineering/domains/infrastructure/terraform/` | Adopt after safety and quality rewrite. Terraform/Terragrunt workflow, validator, and templates are useful. |
| `k8s-troubleshooter` | High | `skills/engineering/domains/infrastructure/kubernetes-troubleshooting/` | Adopt after incident/change-control guardrails. Strong diagnostic structure; keep mutating remediation explicitly gated. |
| `aws-cost-optimization` | Medium | `skills/engineering/domains/cloud/aws-finops/` | Adopt selectively. Replace stale, platform-specific dates and unsupported savings claims; require read-only discovery before any delete/resize/purchase. |
| `ci-cd` | High | `skills/engineering/tools/ci-cd/` | Adopt after security hardening. Clear value, but pin GitHub actions and fix weak examples. |
| `gitops-workflows` | Medium | `skills/engineering/domains/infrastructure/gitops/` | Adopt selectively after current-documentation review; the skill embeds dated product versions and tool recommendations. |
| `monitoring-observability` | Medium-high | `skills/engineering/domains/infrastructure/observability/` | Adopt after command and template repair; its workflow, SLO material, and tools are broadly useful. |

## Claude dependence

The upstream's architecture is Claude Code-specific at the packaging layer:

- root [marketplace manifest](https://github.com/ahmedasmar/devops-claude-skills/tree/1489c33ad8829a11219e423327d6b59f8339cee4/.claude-plugin) and one `.claude-plugin/plugin.json` per skill;
- Claude installation commands in the [upstream README](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/README.md#L59-L78);
- `CLAUDE.md`, which documents the marketplace maintenance model.

AI-hands already uses an open folder convention: `skills/<section>/<skill>/SKILL.md`, with optional `references/`, `templates/`, `assets/`, and `scripts/`. Therefore, omit all `.claude-plugin/` directories and `CLAUDE.md`, move `skills/SKILL.md` to each final skill root, and retain only useful supporting files. Rewrite incidental wording such as “Claude Code can run…” to “Use the available command-execution tool after prerequisite checks.”

## Required adaptation baseline

1. **Use agent-neutral frontmatter and routing.** Preserve `name` and give each description concrete triggers. Make every relative reference point to the new local layout. Add each skill to the appropriate subsection in `skills/engineering/README.md`, then update the count in `skills/README.md`.
2. **Separate read-only diagnosis from mutation.** Default to inspect/plan/diff/validate. Before commands that apply, delete, destroy, terminate, force-unlock, purchase commitments, or change live configuration, require explicit target/environment confirmation, a rollback plan, and post-change verification.
3. **Correct portability defects.** Several AWS and observability examples use BSD/macOS `date -v`; these fail on Linux. Use portable shell helpers or Python. The Terraform module validator has no `--help` handler despite the standard script convention.
4. **Replace time-sensitive assertions with verify-first instructions.** The GitOps skill embeds versions and claims such as ArgoCD `v3.1.9`, Flux `v2.7.1`, and 2025 recommendations. The CI/CD and monitoring material includes unpinned `@main`/`:latest` dependencies and cost/savings claims. Direct agents to official current documentation (and Context7 where available) before using a version, pricing, or recommendation.
5. **Harden templates before agents copy them.** Replace mutable GitHub Action tags (notably `trufflesecurity/trufflehog@main`) with reviewed commit SHAs; use least-privilege permissions; never include production credentials; and label illustrative values. Review every command that can mutate infrastructure.
6. **Keep tools optional and self-contained.** Python scripts compile successfully under Python 3.13 in the assessment environment, and all except the positional-only Terraform validator respond to `--help`. Each skill should state required CLIs, access permissions, dry-run capability, input/output behavior, and an explicit verification step.

## Concrete source-quality findings

- All six main skill documents already use portable `name`/`description` frontmatter and actionable triggers, e.g. [Terraform](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/iac-terraform/skills/SKILL.md), [Kubernetes](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/k8s-troubleshooter/skills/SKILL.md), [CI/CD](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/ci-cd/skills/SKILL.md), [GitOps](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/gitops-workflows/skills/SKILL.md), and [Observability](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/monitoring-observability/skills/SKILL.md). This makes structural conversion low-effort.
- The upstream includes destructive examples: `terraform apply/destroy -auto-approve`, `terraform force-unlock`, `kubectl delete`, Helm deletion, ArgoCD deletion, and cloud-resource stop/terminate guidance. These are not suitable as default autonomous actions.
- The source contains one missing Markdown reference: the Terraform module template links to `./examples/complete`, but the path is absent in the inspected revision.
- The monitoring skill’s Datadog request example has malformed/redacted header text and should be rewritten before reuse. See [the source block](https://github.com/ahmedasmar/devops-claude-skills/blob/1489c33ad8829a11219e423327d6b59f8339cee4/monitoring-observability/skills/SKILL.md#L345-L357).

## Recommended migration order

1. Establish `domains/infrastructure/` and its routing README entry.
2. Port **Kubernetes troubleshooting** and **Terraform** first, as agent-neutral, diagnosis-first skills.
3. Port **CI/CD** with action pinning and an explicit GitHub/GitLab scope.
4. Port **Observability** after fixing Linux date helpers and validating generated dashboard/alert templates.
5. Port **GitOps** and **AWS FinOps** last, replacing all dated vendor-specific claims with “verify current documentation” steps.
6. Run a repository link check, Python compilation, script `--help` smoke tests, Markdown/frontmatter validation, and a fresh safety review before publishing.

## Recommendation

Create native AI-hands skills informed by the upstream material, with source attribution in each new skill’s `README` or provenance section once licensing is explicitly verified. Do **not** import its Claude marketplace metadata, and do **not** use a Git submodule or a verbatim vendor copy. This preserves the useful DevOps knowledge while keeping AI-hands tool- and agent-agnostic, safer for live infrastructure, and maintainable over time.
