---
name: observability
description: Use when investigating metrics, logs, traces, alerts, dashboards, SLI/SLO behavior, alert noise, telemetry cost/cardinality, recording rules, or monitoring-change proposals.
---

# Observability safety and alert triage

**Preserve detection while establishing evidence.** Metrics, logs, traces, and alert routes are operational safety controls. Start with read-only correlation across signals. Do not delete, disable, weaken, or broadly silence an alert just because it is noisy or inconvenient during an incident.

## Scope

Use for vendor-neutral observability investigations and changes. Prometheus/Alertmanager commands are concrete examples; use the approved equivalent for another system. This skill does not authorize access to production logs, traces, customer data, or dashboards—follow existing data-access and incident controls.

## Safety contract

1. Confirm service, environment, cluster/region, telemetry tenant, incident/change ID, affected users, time window/timezone, alert/rule/dashboard identity, owner, and expected impact.
2. Keep initial triage **read-only**. Inspect alert history, evaluated query and labels, SLI/SLO definition, dashboards, target/scrape health, logs, traces, deploy/config history, routing, and notification delivery before proposing a change.
3. Treat telemetry as sensitive: logs, trace attributes, exemplars, labels, queries, links, and dashboards can expose personal data, credentials, internal topology, or customer identifiers. Minimize scope and do not export raw data to unapproved locations.
4. A silence, mute interval, inhibition/routing change, threshold change, rule reload, dashboard/data-source change, sampling change, retention change, or notification change is a mutation. It requires **explicit user or operator confirmation** after the approval gate.
5. Never use an indefinite or broad silence, delete an alert, turn off notifications, or raise a threshold as a diagnostic shortcut. Preserve a recovery signal and a documented owner.

## 1. Establish the measurement boundary

Start with a compact evidence record:

| Item | Confirm |
|---|---|
| User impact | Affected journey/API, actual symptoms, start/end times, population, and business/contract impact |
| Signal | Exact alert/rule ID, query/expression, labels, threshold, `for` duration, notification route, receiver, and alert history |
| Objective | The underlying SLI, SLO window/target, error-budget policy, and whether the alert represents user impact, infrastructure risk, or a diagnostic symptom |
| Telemetry path | Instrumentation/version, collector/agent, scrape/ingest/storage health, data source, retention, sampling, cardinality limits, and access boundary |
| Correlation | Recent deploy/config/traffic/dependency changes and matching metrics, logs, traces, and synthetic checks |

An SLI is a defined quantitative measure; an SLO is a target for that measure. Do not silently substitute a host metric, dashboard panel, or alert threshold for a user-facing SLI/SLO. If the objective is absent or ambiguous, state the uncertainty rather than inventing a target.

## 2. Gather read-only evidence across signals

Follow the timeline: confirm the alert’s actual label set, distinguish pending from firing, inspect the query over an appropriate before/during/after window, then correlate it with deploys, traffic, errors, latency, saturation, dependency signals, logs, and traces.

- **Metrics:** establish collection/target health before diagnosing absence as success. Check label dimensions and query scope; a missing series, scrape failure, stale series, or aggregation change can make a green panel misleading.
- **Logs:** search narrowly by time, service, version, trace/request ID, and approved tenant/identity filters. Do not dump entire production logs or bypass redaction.
- **Traces:** use trace IDs and bounded time windows to locate dependency, retry, queue, and latency paths. Trace sampling can hide rare failures; absence of a trace is not proof of absence.
- **Deploy/config history:** compare immutable revisions and rollout times. A correlation is a hypothesis until the relevant signal supports it.

For local Prometheus rule-file syntax validation, use a clean copy and do not reload a live server as a validation method:

```bash
promtool check rules /path/to/rules.yml
```

`promtool check rules` validates structure, not query correctness, alert routing, cardinality, data availability, or the operational effects of a live reload.

## 3. Diagnose alert quality without removing coverage

| Symptom | Inspect first | Safe direction |
|---|---|---|
| Alert storm | Root alert/event, grouping labels, route tree, deduplication, inhibition, receiver delivery, and dependency topology | Group correlated symptoms and fix the cause; do not blanket silence unrelated alerts. |
| Flapping | Query history, `for`, `keep_firing_for`, evaluation/scrape interval, missing-data semantics, deploys, and dependency behavior | Test a rule change against history; document the detection/response trade-off. |
| False positive | Exact label set, query semantics, recording rules, collector health, SLI definition, and actual user effect | Correct evidence or rule scope with review; do not redefine user impact to make the page disappear. |
| Missing alert | Target/ingest health, rule evaluation, route/receiver state, alert limits, mute/silence/inhibition matchers, and notification delivery | Restore the detection path and independently verify delivery. |
| Telemetry cost or overload | Cardinality, label dimensions, query/rule cost, sample rate, retention, ingestion/drop metrics, and dashboards | Bound high-cardinality labels and validate coverage/cost trade-offs before changing collection or retention. |

Prometheus alerting rules use `for` to delay firing and can use `keep_firing_for` to reduce flapping or false resolution. Alertmanager silences mute notifications only when their matchers apply; they do not fix the underlying condition. Inhibition, grouping, routing, and silences have different effects—record which one is operating before altering any of them.

## 4. Exception and change gate

A narrow operational silence may be justified for an approved maintenance window or a known duplicate page. Before creating one, present:

- exact alert matchers and affected label sets; never a broad wildcard by default;
- a time-boxed start and expiry, named owner, incident/change reference, and removal/verification reminder;
- the reason, expected duration, user-impact assessment, and remaining independent detection/response path;
- evidence that it will not hide a different service, environment, severity, or dependency condition.

A silence is not approval to ignore an active incident. Do not use it to hide a page while changing a rule, deployment, routing tree, or dependency. If no safe narrow scope and expiry can be stated, escalate rather than muting it.

For any live rule, route, dashboard, telemetry, retention, or notification change, obtain explicit user or operator confirmation after presenting:

| Required item | What to state |
|---|---|
| Target | Tenant, environment, rule/route/dashboard/data source, exact labels, file/API revision, and owner |
| Evidence | Alert/query history, correlated signals, SLI/SLO relation, and falsifiable root-cause hypothesis |
| Risk | User detection gap, paging/noise, missing data, data exposure, ingestion/cardinality/cost, availability, and downstream dependencies |
| Change | Exact diff, validation result, peer review, window, approval authority, and whether a live reload is required |
| Verification | Rule evaluation, alert state, notification delivery, dashboard correctness, SLI/SLO behavior, and service health |
| Recovery | Previous immutable config/version, rollback owner, time limit, and stop criteria |

## 5. Verify and record

After an approved change, verify both the monitoring control and the service. Confirm the correct configuration revision is loaded, query results and label sets match expectations, alerts transition as intended, routing/notification reaches the expected receiver, dashboards remain scoped correctly, and the user-facing SLI/SLO did not regress.

If verification is incomplete, the alert becomes broader than reviewed, telemetry cost/cardinality spikes, or a detection gap appears, stop further changes and use the approved rollback. Record final configuration revision, alert/rule IDs, time window, approver, evidence, alert/silence expiry, residual risk, and follow-up owner without copying sensitive telemetry.

## References

- [Prometheus alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) — rule state, `for`, `keep_firing_for`, labels, annotations, and runtime inspection.
- [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) — grouping, inhibition, routing, and time-bounded silences are distinct controls.
- [Prometheus recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) — rule evaluation behavior and `promtool check rules` syntax validation.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — distinguish measured indicators, objectives, and agreements.
- [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/) — metrics, logs, and traces provide complementary evidence.
