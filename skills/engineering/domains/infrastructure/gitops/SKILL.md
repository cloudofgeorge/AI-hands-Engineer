---
name: gitops
description: Use when investigating or reviewing Argo CD or Flux reconciliation, desired-state drift, sync status, GitOps rollbacks, Helm releases, Kustomizations, source revisions, or Git-managed Kubernetes delivery changes.
---

# GitOps safety and reconciliation triage

**Git is the intended change path; reconciliation is a live action.** Establish the desired revision, live target, controller identity, and diff before asking a controller to apply anything. A manual live edit or a forced sync can conceal drift, bypass review, or delete resources.

## Scope

Use for Argo CD and Flux GitOps workflows. Commands differ by product; do not translate flags between them. Pair with Kubernetes troubleshooting for cluster-level symptoms and CI/CD safety for the pipeline that produces the desired revision.

## Safety contract

1. Confirm repository, immutable Git revision, source/OCI artifact digest, application or Kustomization/HelmRelease name, controller instance, cluster/context, namespace, environment, target account, owner, and impact.
2. Start **read-only**. Inspect desired revision, live revision, health/sync/reconciliation status, controller events/logs, rendered manifests, diff, policy results, release history, and ownership before a live action.
3. Treat rendered manifests and controller output as sensitive. They may contain `Secret` metadata, internal endpoints, identifiers, or references to credentials. Do not export or expose secret values.
4. `argocd app sync`, `flux reconcile`, enabling auto-sync, editing source references, applying overlays, Helm upgrades, pruning, rollback, or manual `kubectl` changes are mutations. Each requires **explicit user or operator confirmation** after the approval gate.
5. Do not use manual `kubectl` edits to “fix” a GitOps-managed resource. They create drift and may be overwritten. Do not make `prune`, force options, or auto-sync a default recovery path.

## 1. Establish desired and live boundaries

Record both sides of the reconciliation contract:

| Boundary | Confirm |
|---|---|
| Desired state | Git URL, immutable commit/tree, path, Kustomize/Helm inputs, values, source artifact digest, review/approval, and policy result |
| Live state | Controller instance/identity, Kubernetes context/cluster, namespace, application/release object, current live revision, health, sync/reconcile condition, and resource ownership |
| Delivery | Environment, account/region, maintenance window, dependencies, rollout strategy, cleanup/prune behavior, and rollback revision |

A branch name is not an immutable release identity. If the desired revision and the controller-observed revision differ, investigate the source refresh, cache, access, and reconciliation history before manually changing live resources.

## 2. Read-only diagnosis

For Argo CD, first inspect the named application and the difference between desired and live state:

```bash
argocd app get "$APP"
argocd app history "$APP"
argocd app diff "$APP"
```

`argocd app diff` can exit nonzero when a diff exists; treat that as diagnostic evidence, not an instruction to sync. Record the affected resource addresses, intended revision, health, sync status, hooks/waves, and whether deletion/pruning or immutable-field replacement is involved.

For Flux, inspect controller health and the named reconciliation object before requesting reconciliation:

```bash
flux check
flux get sources all -A
flux get kustomizations -A
flux get helmreleases -A
```

Use the object’s status, observed generation, last attempted/applied revision, conditions, events, and narrowly scoped controller logs to distinguish source fetch, decryption, render, policy, dependency, Helm, apply, and readiness failures. `flux reconcile` is not a read-only diagnostic command: it asks the controller to reconcile and can cause it to apply the current desired state.

## 3. Diagnose common divergence safely

| Symptom | Inspect first | Safe direction |
|---|---|---|
| OutOfSync / drift | Immutable desired revision, live diff, manager/owner, controller history, and recent manual changes | Fix the reviewed desired state or explicitly accept a known controller-owned difference; do not patch live state to hide it. |
| Degraded / not ready | Resource health, events, controller condition, rollout/release history, dependencies, and Kubernetes evidence | Identify the failed layer before changing values or re-syncing. |
| Source not fetched | Source URL/revision/digest, auth reference existence, controller logs, network, and source status | Restore access through the approved secret/identity path; do not disclose or replace credentials ad hoc. |
| Reconciliation loop | Changed revisions, generated artifacts, dependency graph, health checks, prune behavior, and controller errors | Stop uncontrolled change promotion and investigate the loop; do not repeatedly force reconcile. |
| Unexpected deletion | Diff, prune settings, resource ownership, orphan/retention policy, Helm hooks, and data/PVC implications | Stop before sync; require named-resource approval and recovery/retention decision. |

Never delete an application, source, Helm release, namespace, or controller installation as a troubleshooting shortcut. Reconcile only a reviewed desired revision; it is not equivalent to a harmless refresh.

## 4. Approval gate for a GitOps mutation

Before a sync, reconcile, source change, auto-sync/auto-prune enablement, Helm/overlay change, rollback, or manual recovery, present:

| Required item | What to state |
|---|---|
| Exact target | Controller, app/object, cluster/context, namespace, desired immutable revision, source artifact digest, and resource scope |
| Evidence | Diff, observed/live revisions, conditions/events, policy/CI result, and evidence-backed hypothesis |
| Risk | Creates, updates, replacements, `prune`/deletion, hooks, CRDs, Secrets, data/PVCs, network/IAM, availability, and dependency effects |
| Change | Exact Git diff or controller action, peer review, owner, window, concurrency behavior, and approval authority |
| Verification | Reconciled revision, health/readiness, rollout, application checks, synthetic signals, alert state, and drift check |
| Recovery | Previously verified immutable revision/artifact, Git revert/rollback owner, restore requirements, and stop criteria |

For a rollback, prefer a reviewed Git revert or a documented controller-supported rollback to a known immutable revision. A historical revision being available is not evidence that it is safe for current data/schema/dependencies. Re-render/review the resulting diff and obtain approval again.

## 5. Verify and record

After an approved action, verify that the controller observed exactly the intended revision, applied only the reviewed resource scope, completed hooks/waves, reached health/readiness, and left no unexpected diff or prune. Then verify the workload through the relevant application and observability signals.

If scope, deletion, health, or revision differs from the reviewed plan, stop further reconciliation, preserve controller/diff evidence, and use the approved rollback/recovery path. Record revision/digest, controller/object, environment, approver, timestamps, result, residual drift, and follow-up owner without storing credentials.

## References

- [Argo CD sync options](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/) — sync behavior and options can change live resources.
- [Argo CD sync waves](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/) — ordering and hooks affect rollout scope.
- [Flux troubleshooting](https://fluxcd.io/flux/cheatsheets/troubleshooting/) — inspect conditions, sources, events, and controller logs.
- [Flux reconcile kustomization](https://fluxcd.io/flux/cmd/flux-reconcile-kustomization/) — reconcile is a controller request, not a read-only inspection.
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) — treat Secret data and references as sensitive operational material.
