---
name: troubleshooting-kubernetes
description: Use when investigating Kubernetes or K8s incidents, failing Pods, CrashLoopBackOff, Pending workloads, Service connectivity, NetworkPolicies, permissions, or rollout health in a cluster.
---

# Kubernetes troubleshooting

**Evidence before mutation.** Establish the exact cluster, namespace, impact, and observed state before proposing a change. This skill is agent-neutral: it works with `kubectl`, human operators, and any approved deployment system.

## Scope

Use for diagnosis of workloads, Services, scheduling, permissions, and network policy effects. Start with read-only inspection; hand off an approved remediation to the deployment or incident process. Do not use this skill to perform unapproved production changes.

## Safety contract

1. State the environment, current kubeconfig context, namespace, affected workload, symptom, start time, and customer impact. Do not infer any of them from a resource name.
2. Use an explicit `-n "$NAMESPACE"` on namespaced commands. Do not rely on a default namespace.
3. Check read permission before broad inspection. If access is denied, report the missing permission; do not bypass RBAC, TLS validation, or cluster policy.
4. Keep diagnosis **read-only**. `kubectl exec`, `kubectl debug`, port forwarding, changing replicas, deleting Pods, changing Helm releases, changing NetworkPolicies, and rollout actions are mutations or live interventions.
5. A live change requires **explicit user confirmation** after presenting: target context/namespace, evidence-backed hypothesis, exact change, expected effect, verification command, rollback method, and blast radius.

## 1. Establish the boundary

Set variables only after the operator has named the intended target:

```bash
CONTEXT="<approved-context>"
NAMESPACE="<approved-namespace>"
WORKLOAD="<deployment-or-statefulset>"

kubectl config current-context
kubectl --context="$CONTEXT" cluster-info
kubectl --context="$CONTEXT" auth can-i list pods -n "$NAMESPACE"
kubectl --context="$CONTEXT" auth can-i get pods --subresource=log -n "$NAMESPACE"
```

If `current-context` differs from the approved context, stop and resolve the discrepancy before querying resources.

## 2. Capture a small evidence set

Start narrowly with the affected namespace and workload. Save command output with timestamps in the incident record when the environment allows it.

```bash
kubectl --context="$CONTEXT" get pods -n "$NAMESPACE" -o wide
kubectl --context="$CONTEXT" get deploy,statefulset -n "$NAMESPACE"
kubectl --context="$CONTEXT" get events -n "$NAMESPACE" --sort-by='.metadata.creationTimestamp'
kubectl --context="$CONTEXT" get pod -n "$NAMESPACE" -l "app=<label>" -o yaml
```

For a single Pod, inspect state, ownership, events, current logs, and logs from the prior container instance:

```bash
POD="<pod>"
CONTAINER="<container>"

kubectl --context="$CONTEXT" describe pod "$POD" -n "$NAMESPACE"
kubectl --context="$CONTEXT" logs "$POD" -c "$CONTAINER" -n "$NAMESPACE" --tail=200
kubectl --context="$CONTEXT" logs "$POD" -c "$CONTAINER" -n "$NAMESPACE" --previous --tail=200
```

`--previous` is relevant only when the container has restarted. Record the controller (`Deployment`, `StatefulSet`, `Job`, or unmanaged Pod) before considering remediation; deleting a controller-managed Pod only causes reconciliation and is rarely root-cause work.

## 3. Follow the symptom branch

| Symptom | Inspect first | Common evidence-backed direction |
|---|---|---|
| `CrashLoopBackOff` | `describe`, current and previous logs, command/args, probes, exit code, requests/limits | Application startup/configuration failure, probe failure, dependency failure, or resource pressure. Do not restart blindly. |
| `Pending` | Pod events, node selectors/affinity, taints/tolerations, requests, quota | Scheduler evidence distinguishes insufficient resources, constraints, quota, or unbound storage. |
| `ImagePullBackOff` / `ErrImagePull` | Pod events, image name/tag/digest, image pull secret references | Validate registry reachability and credentials through the approved secret/deployment path; do not expose secret values. |
| Service has no response | Service selector/ports, EndpointSlices, ready Pods, DNS from an approved diagnostic location | Confirm a matching ready endpoint before blaming DNS, kube-proxy, or NetworkPolicy. |
| Permission denied | Exact API error and `kubectl auth can-i` result | Request the least additional RBAC permission required; never broaden access speculatively. |
| Network path failure | Service/EndpointSlices, Pod labels, applicable ingress and egress policies, CNI support | NetworkPolicies are additive and may be enforced by the CNI. Identify both source and destination before proposing a policy edit. |

### Service and NetworkPolicy evidence

```bash
SERVICE="<service>"

kubectl --context="$CONTEXT" get service "$SERVICE" -n "$NAMESPACE" -o yaml
kubectl --context="$CONTEXT" get endpointslice -n "$NAMESPACE" \
  -l "kubernetes.io/service-name=$SERVICE" -o yaml
kubectl --context="$CONTEXT" get networkpolicy -n "$NAMESPACE" -o yaml
kubectl --context="$CONTEXT" get pods -n "$NAMESPACE" --show-labels
```

Never remove, weaken, or “temporarily disable” a NetworkPolicy merely to test connectivity. The policy may protect unrelated traffic, and policy behavior depends on the installed network plugin. Instead, map source labels, destination labels, ports, namespaces, and both ingress/egress policy selection.

For generalized cluster slowness, first separate connectivity failures from capacity, DNS, control-plane, storage, or application latency. Use the approved monitoring and CNI runbook to inspect the relevant CNI controller and node components in their explicitly named system namespace. CNI resource names and metrics are implementation-specific; do not guess them, and never disable a policy as a diagnostic shortcut.

### Helm release evidence

When a Helm release is implicated, first preserve its read-only diagnostic state. Confirm that Helm is installed and the release, context, namespace, chart reference, and environment are the intended targets.

```bash
RELEASE="<release>"

helm status "$RELEASE" -n "$NAMESPACE"
helm history "$RELEASE" -n "$NAMESPACE"
helm get values "$RELEASE" -n "$NAMESPACE" --all
helm get manifest "$RELEASE" -n "$NAMESPACE"
```

A pending or failed release is not evidence that uninstalling it is the correct fix. Before proposing an approved uninstall, reinstall, or rollback, capture the exact chart version or digest, effective values, release history, manifests, hooks, relevant events, and data/PVC implications. A live Helm action remains a production mutation under the approval gate.

## 4. Propose, preview, then change only with approval

Summarize the evidence as a falsifiable hypothesis. For example: “Pod is unschedulable because events show `FailedScheduling` for insufficient CPU; no configuration change is evidenced yet.”

For a rollback proposal, preview the target before executing a live action:

```bash
kubectl --context="$CONTEXT" rollout history "deployment/$WORKLOAD" -n "$NAMESPACE"
kubectl --context="$CONTEXT" rollout undo --dry-run=server "deployment/$WORKLOAD" -n "$NAMESPACE"
```

A preview is not approval. Before any live mutation, obtain explicit user confirmation and state:

- target context and namespace;
- change owner and exact resource revision;
- success signal (`rollout status`, ready replicas, synthetic check, or application metric);
- rollback command or GitOps revision; and
- observation window and escalation condition.

## 5. Verify and close

After an approved change, verify the defined success signal rather than just a `Running` Pod:

```bash
kubectl --context="$CONTEXT" rollout status "deployment/$WORKLOAD" -n "$NAMESPACE" --timeout=5m
kubectl --context="$CONTEXT" get pods -n "$NAMESPACE" -l "app=<label>"
kubectl --context="$CONTEXT" get events -n "$NAMESPACE" --sort-by='.metadata.creationTimestamp'
```

Record the hypothesis, evidence, approved action, verification result, rollback readiness, and any follow-up required to prevent recurrence.

## Official references

- [Debug running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
- [Debug Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
- [Pod lifecycle and container states](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- [NetworkPolicies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [`kubectl auth can-i`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/)
- [`kubectl rollout undo`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/)
- [Helm release inspection: status, history, values, and manifests](https://helm.sh/docs/helm/helm_status/)
