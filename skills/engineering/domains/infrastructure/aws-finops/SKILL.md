---
name: aws-finops
description: Use when investigating AWS cost or usage changes, Cost Explorer, Cost and Usage Reports, Budgets, tagging allocation, spend anomalies, Savings Plans, Reserved Instances, or cloud-cost optimization proposals.
---

# AWS FinOps safety and cost analysis

**Measure before optimizing.** Cost data is delayed, estimated, scoped by account and billing model, and can contain sensitive resource or allocation metadata. Establish a reproducible read-only baseline before changing a resource, budget, IAM policy, purchase commitment, or data-export configuration.

## Scope

Use for AWS cost/usage investigation and FinOps recommendations. It does not authorize cloud resource changes, account/organization changes, or commitments. Pair with Terraform, GitOps, CI/CD, and service-owner controls for changes that affect live workloads.

## Safety contract

1. Confirm AWS partition, management/member account and payer relationship, organization scope, IAM role, region, currency, billing period/timezone, cost metric, granularity, filters/groupings, allocation/tag policy, owner, and business/workload impact.
2. Start **read-only**. Inspect identity, Cost Explorer/CUR data, budget/anomaly history, resource inventory, tags, utilization, commitment coverage, credits/discounts, and workload/SLO evidence before proposing a change.
3. Current-month cost and usage can be **estimated** and later corrected; data may arrive late. Do not claim savings, root cause, or allocation certainty without the query scope, time window, metric, and uncertainty recorded.
4. Budget actions, CUR/Data Export delivery, IAM changes, tag-policy enforcement, resource scheduling/rightsizing, deletion, commitment purchase/exchange, or any workload modification requires **explicit user or operator confirmation** after the approval gate.
5. Follow least privilege. Billing visibility, CUR buckets, Cost Explorer APIs, resource tags, and linked-account metadata may be commercially or operationally sensitive; do not broaden billing/IAM access or export raw reports by default.

## 1. Establish identity and billing scope

First verify the active identity and then obtain explicit confirmation that it is the intended billing/account scope:

```bash
aws sts get-caller-identity
```

Record whether the analysis is at management-account, member-account, organization, or linked-account scope. Confirm whether costs are unblended, amortized, net, blended, or another approved metric; whether taxes, support, refunds, credits, and discounts are included; and whether dates are complete billing periods or in-progress estimates.

Do not infer account ownership from an account alias, repository name, or a single resource. If the identity or billing visibility differs from the approved scope, stop before querying or changing anything.

## 2. Reproduce a read-only baseline

Use a bounded, documented date range and dimensions. For example, Cost Explorer can be queried read-only with an explicitly selected metric and grouping:

```bash
aws ce get-cost-and-usage \
  --time-period Start=<YYYY-MM-DD>,End=<YYYY-MM-DD> \
  --granularity DAILY \
  --metrics UnblendedCost UsageQuantity \
  --group-by Type=DIMENSION,Key=SERVICE
```

The `End` date is exclusive. Cost Explorer API calls can incur a per-request charge, so avoid unbounded polling and record query parameters. Cost Explorer data is not necessarily final; compare like-for-like periods and explain currency, granularity, data freshness, metric, filters, groupings, and allocation coverage.

For deeper attribution, use the approved Cost and Usage Report (CUR) or AWS Data Exports path. CUR data is delivered to an owned S3 bucket, can be updated multiple times per day, is cumulative within the month, and may include resource IDs, tags, and other sensitive metadata. Query only the approved partition/table with least-privilege access; do not copy raw CUR data to chat, public storage, or unapproved analytics tools.

## 3. Form an evidence-backed recommendation

Separate observations from interventions:

| Observation | Required evidence before a recommendation |
|---|---|
| Spend anomaly | Baseline/comparison window, service/operation/region/account dimensions, usage change, deployments/incidents, credits/refunds, and data freshness |
| Idle or oversized resource | Resource identity/owner, utilization over a representative period, workload schedule, performance/SLO headroom, dependencies, and recovery method |
| Tag/allocation gap | Tag policy/activation, coverage percentage, account/service exceptions, owner mapping, and effect on the selected cost metric |
| Commitment opportunity | Eligible usage history, utilization/coverage, baseline volatility, term/payment risk, expiration schedule, break-even assumptions, and approval authority |
| Budget concern | Actual and forecasted spend, threshold/period/filters, notification recipient, delay behavior, linked-account scope, and effect of any action |

A cost-saving estimate must state its assumptions, baseline, time window, metric, confidence/range, implementation cost, service/SLO risk, owner, and how actual savings will be measured. Do not recommend deleting, stopping, resizing, or scheduling resources from cost data alone.

## 4. Guardrails for budgets and commitments

AWS Budgets can notify on actual or forecasted spend and can apply actions; billing data and notifications have delay. Treat a Budget update, deletion, notification destination, or action as a production control change. Do not make a budget action that denies provisioning or changes IAM policy without named account scope, stakeholder approval, tested exception path, owner, expiry/review policy, and rollback.

Savings Plans and Reserved Instances are financial and capacity commitments, not generic “discount buttons.” Before a purchase, exchange, modification, or renewal, require explicit approval of eligible usage, coverage/utilization, term, payment option, account allocation, forecast assumptions, break-even sensitivity, workload migration/termination risk, commitment owner, accounting/procurement policy, and exit/exception constraints. A past utilization graph is not a commitment approval.

## 5. Approval gate for optimization changes

Before any resource, budget, export, IAM, tag-policy, or commitment change, present:

| Required item | What to state |
|---|---|
| Target | Accounts, regions, resources/budget/export/commitment IDs, owner, and exact billing/query scope |
| Evidence | Reproducible query, data freshness, metric, baseline/comparison, utilization and workload/SLO evidence, and assumptions |
| Risk | Availability, performance, data, security/IAM, compliance, cost reallocation, notification/control gap, and commitment lock-in |
| Change | Exact action, owner, peer/finance review, maintenance window, policy/procurement approval, and dependencies |
| Verification | Service/SLO health, resource state, actual cost/usage metric and expected reporting delay, budget/notification behavior, and allocation result |
| Recovery | Reversible configuration/reprovision plan, budget/IAM restoration, commitment escalation path, stop criteria, and incident owner |

Never use `terminate`, deletion, blanket stop/schedule actions, unreviewed IAM denial, or long-term purchase as a cost-anomaly shortcut. When an intervention is not safely reversible, make that explicit and escalate to the accountable engineering and finance owners.

## 6. Verify and record

After an approved change, verify the workload and financial controls separately: application/SLO health, resource/automation state, tag/allocation behavior, budget notifications, and the resulting like-for-like cost/usage trend after the documented reporting delay. Do not declare savings until the metric, period, and confounders support the conclusion.

Record account scope, role, query/data-source parameters, metric, time window, freshness, baseline, assumptions, approval, action, verification date, residual risk, and owner. Store links or restricted evidence rather than raw billing exports or sensitive resource data.

## References

- [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) — delivery, granularity, cumulative/estimated updates, and sensitive report detail.
- [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) — history, forecast, data-refresh behavior, and API usage cost.
- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) — actual/forecast notifications, actions, and reporting delay.
- [AWS Billing IAM guidance](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html) — least privilege and IAM policy validation.
- [AWS Well-Architected Cost Optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) — ongoing cost management across technology and finance.
