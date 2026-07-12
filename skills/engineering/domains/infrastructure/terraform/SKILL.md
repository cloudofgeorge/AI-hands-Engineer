---
name: terraform
description: Use when investigating or reviewing Terraform, OpenTofu-compatible Terraform workflows, Terragrunt wrappers, plans, state locks, drift, workspaces, backends, imports, or infrastructure change proposals.
---

# Terraform safety and diagnosis

**Identify the state boundary before changing it.** Terraform can alter remote infrastructure and state. Start with a narrow, read-only evidence set; treat plans, state, variables, and backend configuration as potentially sensitive; and do not turn an urgent request into an unreviewed mutation.

## Scope

Use for native Terraform CLI workflows and Terraform-compatible tooling. For Terragrunt, first identify its version, generated working directory, selected stack, and the exact Terraform command it will invoke; retain the same safety contract. Do not assume that a directory name, cloud account alias, or workspace name proves the intended environment.

## Safety contract

1. Name and confirm the repository revision, working directory, Terraform distribution/version, backend, workspace, cloud account or subscription, region, target stack, owner, incident/change reference, and expected customer impact.
2. Do not run commands from an unverified directory. A workspace is not a sufficient account boundary; record the backend and provider identity separately.
3. Keep initial triage **read-only**. Avoid printing or copying secret values, full state, `.tfvars`, plan files, environment variables, cloud credentials, or backend credentials into chat, tickets, logs, or version control.
4. `terraform init` changes local working-directory metadata and can contact registries, modules, and the configured backend. Use `terraform init -backend=false` only for offline structural validation. Initialize against a real backend only after the target boundary is confirmed.
5. A live mutation requires **explicit user or operator confirmation** after presenting the exact target, evidence-backed rationale, full plan/diff, affected resources, irreversible or data-loss risk, maintenance/approval record, verification signal, rollback or recovery path, and blast radius.

## 1. Establish the boundary

Set variables only after the operator has named the intended target. Never replace these with guessed names from the repository.

```bash
REPO="<approved-repository-path>"
REF="<approved-revision>"
BACKEND="<approved-backend-and-state-key>"
WORKSPACE="<approved-workspace>"
ACCOUNT="<approved-cloud-account-or-subscription>"
REGION="<approved-region>"

cd "$REPO"
git rev-parse --show-toplevel
git status --short
git rev-parse HEAD
terraform version
```

Confirm that the checked-out revision matches `REF`. Inspect the backend declaration and provider configuration without emitting credentials. If a wrapper is involved, inspect its configuration and use its supported inspection command before running Terraform in a generated directory.

Before any remote-state interaction, require the operator to confirm `BACKEND`, `WORKSPACE`, `ACCOUNT`, and `REGION` independently. Stop if they disagree with the observed configuration or expected environment.

## 2. Perform safe structural checks

For a reusable module that does not require its production backend, validate the configuration without backend access:

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
```

`terraform validate` checks configuration syntax and internal consistency; it does not validate provider APIs or remote state. `terraform init -backend=false` still writes local `.terraform` data and can download providers/modules, so use an approved disposable or clean working copy and do not commit generated files.

For an initialized, explicitly approved target, identify the selected workspace and available workspaces before planning:

```bash
terraform workspace show
terraform workspace list
terraform providers
```

A command failing because the directory is uninitialized is evidence, not a reason to run an unscoped `init`, select a workspace, or create backend resources.

## 3. Inspect drift and a speculative plan

A normal `terraform plan` is non-infrastructure-mutating: it reads current remote objects and compares them with configuration, but does not execute the proposed changes. When the selected backend supports locking, it can acquire an operation lock and temporarily block concurrent work. Before running it, confirm the backend/workspace and that this temporary lock is acceptable; do **not** bypass it with `-lock=false`. Start with a speculative plan and review it as a change artifact.

```bash
terraform plan -input=false -no-color
terraform plan -refresh-only -input=false -no-color
```

Use the normal plan to identify proposed creates, updates, replacements, and destroys. Use `-refresh-only` only to examine reconciliation of Terraform state with out-of-band changes; it is not a remedy for drift by itself. Record:

- resource addresses and provider/account/region;
- counts and identities of creates, changes, replaces, and destroys;
- immutable-resource replacement, public exposure, IAM, networking, data, and cost effects;
- whether provider data, variables, or sensitive values are redacted or need restricted review.

Do not make `-target`, `-replace`, `-destroy`, `-refresh-only`, `-refresh=false`, `-invoke`, `-parallelism`, `-lock=false`, `-var`, or `-var-file` a routine shortcut. Each changes the meaning or safety of the plan and needs a documented reason and an explicit approval boundary. `-refresh=false` skips synchronization with remote objects, so its output may not reflect current drift and cannot by itself support an apply approval. `-invoke` creates a plan for the named action while excluding all other configuration, so confirm the action identity and effects explicitly and never treat that plan as evidence that the rest of the configuration is safe. Never use a targeted plan to claim that the rest of the configuration is safe.

## 4. State and lock incidents

State is sensitive operational data and may contain secrets. Prefer metadata-level inspection and approved secure storage over exporting the complete state. Do not paste `terraform state pull` output, plan files, provider credentials, or decrypted variable files into an issue.

If Terraform reports a lock:

1. capture the exact lock ID, holder, operation, timestamp, backend, workspace, and intended target;
2. verify whether the holder is an active approved operation through the incident/change owner and backend audit evidence;
3. wait for or coordinate with the owner when the lock is active or ownership is uncertain;
4. do **not** bypass locking with `-lock=false`.

`terraform force-unlock` removes a state lock but does not modify infrastructure. It can still enable conflicting writers, so use it only for a demonstrably abandoned lock owned by the authorized team, with the exact backend/workspace and lock ID confirmed. It remains a mutation and requires explicit user or operator confirmation before the command:

```bash
# Run only after the approval gate and ownership checks above.
terraform force-unlock "$LOCK_ID"
```

Treat `terraform import`, `terraform state mv`, `terraform state rm`, `terraform state push`, workspace creation/deletion, backend migration, and provider upgrades as state or control-plane changes. They require their own scoped change plan, backup/recovery method, peer review, and approval; they are never incident shortcuts.

## 5. Approval gate for apply or destroy

Do not run `terraform apply`, `terraform destroy`, import, state mutation, or backend migration from a conversational instruction alone. Before a live action, present a compact decision record:

| Required item | What to state |
|---|---|
| Exact target | Repository revision, directory, backend/state key, workspace, provider account/subscription, region, and resource addresses |
| Evidence | Current symptoms, plan timestamp, plan summary, and why this change addresses the hypothesis |
| Risk | Destroys, replacements, data, IAM, network, availability, cost, concurrent writers, and dependent systems |
| Control | Change owner, required peer review, maintenance window, approval authority, and secret-handling path |
| Verification | Provider/Kubernetes/application health signals, alert expectations, and owner for acceptance |
| Recovery | Tested rollback, restore, import/state recovery method, and criteria to stop |

A reviewed plan can become stale when another change lands. Regenerate and review the final plan immediately before an approved apply. If a saved plan file is part of the approved release process, restrict its access, do not commit it, verify it was created for the same configuration/workspace/backend, and apply only that reviewed artifact through the approved automation. A plan preview is not approval.

For any destroy or plan containing unexpected destruction, stop. Require explicit confirmation that names every destructive resource or intentionally scoped environment, plus a recovery and retention decision. Never normalize non-interactive approval flags as a default.

## 6. Verify and record

After an approved mutation, verify the declared success signal rather than only a zero exit code:

1. run the approved post-change plan or refresh-only plan and confirm the expected result;
2. inspect provider and application health through the approved monitoring/runbook path;
3. confirm no unexpected lock, drift, alert, cost anomaly, or dependent-service regression remains;
4. record the final revision, backend/workspace, plan summary, approver, timestamps, evidence links, and follow-up owner without recording sensitive values.

If verification fails or the blast radius differs from the reviewed plan, stop further mutation, preserve evidence, escalate through the incident/change process, and use only the approved recovery path.

## References

- [Terraform plan command](https://developer.hashicorp.com/terraform/cli/commands/plan) — plans are previews; normal and refresh-only planning modes have different intent.
- [Terraform validate command](https://developer.hashicorp.com/terraform/cli/commands/validate) — `validate` is safe for configuration verification; `init -backend=false` supports backend-free validation.
- [Terraform state locking](https://developer.hashicorp.com/terraform/language/state/locking) — do not disable locks; force-unlock only a known, failed lock owned by your team.
- [Terraform force-unlock command](https://developer.hashicorp.com/terraform/cli/commands/force-unlock) — exact lock ID and backend behavior matter.
- [Terraform workspace show](https://developer.hashicorp.com/terraform/cli/commands/workspace/show) — verifies the currently selected workspace.
