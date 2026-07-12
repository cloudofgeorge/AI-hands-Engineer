---
name: ci-cd
description: Use when investigating, reviewing, or changing GitHub Actions or GitLab CI pipelines, deployment gates, runners, artifacts, secrets, workflow triggers, or release rollbacks.
---

# CI/CD safety and incident triage

**Evidence before bypass.** A pipeline is production automation with identities, secrets, artifacts, and deployment authority. Diagnose the failed run and its trust boundary before changing a trigger, permissions, runner, secret, branch rule, or deployment gate.

## Scope

Use for GitHub Actions and GitLab CI. First identify which platform and runner execute the pipeline; their syntax and trust controls are not interchangeable. This skill covers workflow/pipeline review and safe release control, not a substitute for the platform’s deployment, security, or incident process.

## Safety contract

1. Confirm repository, immutable revision, platform, workflow/pipeline file, job, run ID, trigger/event, actor, runner type, environment, artifact digest, target account/cluster/region, and customer impact.
2. Keep initial work **read-only**: inspect configuration at the failing revision, job summary, logs with redaction preserved, event payload metadata, environment/deployment history, artifact metadata, runner status, and audit trail.
3. Treat code and configuration from forks, pull requests, external contributors, and untrusted inputs as hostile until the trigger, token permissions, secret scope, checkout ref, and runner isolation are reviewed.
4. Never print, decode, reformat, pass through, or request secrets in logs, comments, workflow files, shell tracing, or chat. Masking reduces accidental exposure but does not make hostile pipeline code safe.
5. Editing a workflow, re-running a privileged job, approving an environment, rotating a credential, changing a runner, publishing an artifact, promoting/redeploying, or rolling back is a mutation. It requires **explicit user or operator confirmation** after the approval gate below.

## 1. Establish the execution and trust boundary

Create an evidence record before proposing a fix:

| Boundary | Confirm |
|---|---|
| Source | Repository, immutable SHA, workflow or `.gitlab-ci.yml` path, include/reusable-workflow revisions, and changed lines |
| Trigger | Event/pipeline source, actor, branch/tag, pull request/fork status, manual inputs, schedule, and any downstream trigger |
| Identity | `GITHUB_TOKEN` or GitLab job-token permissions, cloud identity, OIDC audience/subject, secret/variable scope, and environment protection |
| Execution | Hosted or self-hosted runner, runner group/tags, image, network reachability, cache, concurrency group, and isolation boundary |
| Delivery | Artifact name and digest, provenance/attestation if available, deployment environment, account/cluster/region, and rollback artifact |

Do not infer a production target from `main`, a job name, or a successful earlier run. If the revision, environment, or cloud identity is ambiguous, stop and resolve that discrepancy before re-running or editing anything.

## 2. Read-only failure triage

Start with the smallest evidence set: the failed step, first causal error, exit status, job dependencies, event/actor, runner identity, and deployment history. Compare the failing revision against the last known-good revision and distinguish configuration, source, dependency, secret/permission, runner, artifact, and downstream-service failures.

For GitHub Actions, inspect the workflow at the run’s commit and the run/job summary. For GitLab, inspect the pipeline source, `.gitlab-ci.yml` plus included files, evaluated job `rules`, runner tags, and protected-ref/variable configuration. Preserve log redaction; do not enable debug tracing in a privileged production run merely to obtain more detail.

A retry is evidence only if it leaves the same trust boundary intact. Do not retry a job that could expose secrets, publish an artifact, deploy, mutate state, or execute unreviewed fork code until its identity and inputs are understood.

## 3. Secure workflow design review

### GitHub Actions

- Set explicit `permissions:` at workflow or job scope and follow **least privilege**. Start `GITHUB_TOKEN` permissions read-only and grant only the capability a job demonstrably needs.
- Pin third-party actions and reusable workflows to a verified **full-length commit SHA**. A tag is mutable; validate the owner, source, commit, release/update process, and required permissions before pinning.
- Prefer short-lived federation through OIDC over long-lived cloud credentials. Scope OIDC trust policies to the repository, ref, environment, audience, and job context required by the deployment; `id-token: write` is itself a privileged grant.
- Do not combine a privileged `pull_request_target` or `workflow_run` trigger with checkout or execution of untrusted pull-request code. These triggers can access main-branch caches, write permissions, or secrets. Separate untrusted build/test work from privileged labeling or deployment work.
- Treat expressions sourced from issue titles, branch names, commit messages, pull-request fields, dispatch inputs, or API data as untrusted. Pass them via an intermediate environment variable or trusted action interface rather than interpolating them into shell syntax.
- Use protected environments and required reviewers for production deployment. An approval UI click does not replace review of the exact artifact, target, identity, and rollout plan.

### GitLab CI

- Keep sensitive variables out of `.gitlab-ci.yml`; store them in the approved secret/variable system, scope them to protected branches/tags and environments, and review all CI configuration changes before running them.
- Treat pipelines run in a parent project for a fork as privileged: protected or masked variables may become available. Do not run unreviewed fork configuration in a context that can access sensitive variables or runners.
- Review `rules` in order and record the first matching rule. Rules are evaluated before scripts run, so a variable created by a job cannot safely determine whether that job is included. Avoid broad final rules that accidentally start duplicate push and merge-request pipelines.
- Confirm runner tags, protected runner access, includes, child/downstream pipeline variable forwarding, and environment scope before changing a job’s execution context.

## 4. Artifact and release integrity

A green build is not sufficient release evidence. Record the source SHA, dependency/lockfile revision, build command, runner, artifact name, immutable digest, signature or provenance when available, test results, vulnerability/policy checks, and intended target.

Do not rebuild and silently substitute an artifact after approval. If the source, configuration, dependencies, or artifact digest changes, regenerate review evidence and obtain approval again. Keep artifact retention, access, and promotion aligned with the incident/change record; do not use an unverified latest tag for rollback.

## 5. Approval gate for deployment changes

Before changing a workflow, granting extra permissions, bypassing a required check, manually triggering a production job, promotion, deployment, or rollback, present:

| Required item | What to state |
|---|---|
| Target | Repository SHA, pipeline/run ID, environment, account/cluster/region, runner, artifact digest, and affected service |
| Evidence | First causal failure, configuration diff, trigger/actor, runner and identity details, and reason the proposed action addresses it |
| Risk | Secrets, privileged tokens, untrusted code, data, availability, network/IAM, supply chain, cost, and concurrent-release effects |
| Change | Exact YAML/config/UI/API operation, required peer review, owner, window, and approval authority |
| Verification | Job and deployment health, version/digest at target, application metrics, synthetic checks, and alert expectations |
| Recovery | Approved rollback artifact/revision, abort criteria, state/data implications, and escalation owner |

Do not “fix” an urgent failure by disabling tests, branch protection, required reviewers, artifact verification, secret masking, protected variables, or deployment gates. If a temporary exception is approved, time-box it, name its owner, preserve the original control, and create a follow-up to remove the exception.

## 6. Verify, recover, and record

After an approved change, verify the intended immutable artifact and deployment target, then observe application-level health rather than treating a CI exit code as success. Confirm that the expected environment, version/digest, identity, tests, checks, metrics, and alerts are correct.

If verification fails, stop promotion, preserve the run/configuration evidence, and use the approved rollback artifact or release process. Do not rerun privileged pipelines repeatedly or roll back to an unverified mutable tag. Record final source SHA, artifact digest, environment, approver, timestamps, evidence links, residual risk, and follow-up owner without storing secrets.

## References

- [GitHub Actions secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, full-length commit SHA pinning, secret handling, untrusted-code checkout, and protected environments.
- [GitHub Actions workflow triggers](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow) — events, filters, manual inputs, and environment approvals.
- [GitHub Actions deployment security](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments) — OIDC-based cloud authentication.
- [GitLab CI/CD variables](https://docs.gitlab.com/ci/variables/) — sensitive-variable handling, fork trust boundaries, protected variables, and masking limits.
- [GitLab job rules](https://docs.gitlab.com/ci/jobs/job_rules/) — first-match evaluation and avoiding unintended duplicate pipelines.
