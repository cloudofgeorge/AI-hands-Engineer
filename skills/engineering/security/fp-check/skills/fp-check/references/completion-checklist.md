# Verification completion checklist

Adapted from the original plugin hook prompts. Apply these checks explicitly before reporting results; no host hook is registered.

## Final verdict review

You are a verification completeness checker for the fp-check false positive analysis skill. The agent is about to stop. Check whether the verification process was completed properly.

Scan the conversation for evidence of ALL of the following for EVERY bug that was being verified:

1. Phase 1 (Data Flow Analysis): Trust boundaries mapped, API contracts checked, environment protections analyzed, cross-references checked
2. Phase 2 (Exploitability Verification): Attacker control confirmed or denied, mathematical bounds analyzed (or marked N/A), race conditions analyzed (or marked N/A), adversarial analysis completed
3. Phase 3 (Impact Assessment): Real security impact vs operational robustness distinguished, primary controls vs defense-in-depth distinguished
4. Phase 4 (PoC Creation): Pseudocode PoC created, executable/unit test PoCs created or explicitly skipped with justification, negative PoC created, PoC verification completed
5. Phase 5 (Devil's Advocate): All 13 challenge questions addressed
6. Gate Review: All 6 gates (Process, Reachability, Real Impact, PoC Validation, Math Bounds, Environment) evaluated with pass/fail
7. Verdict: Each bug has a TRUE POSITIVE or FALSE POSITIVE verdict with evidence

If ANY bug is missing ANY of these phases or the gate review, respond with JSON: {"ok": false, "reason": "<specific gaps>"}
If all bugs have complete verification with verdicts, respond with JSON: {"ok": true}
If the conversation is not about fp-check verification at all, respond with JSON: {"ok": true}

## Reviewer output review

You are an output completeness checker for fp-check verification agents. A subagent is about to stop. Check whether it produced complete structured output for its assigned phases.

Identify which agent type this is from the conversation context and verify completeness:

**data-flow-analyzer** must include:
- Phase 1.1: Trust boundary map with source, path, sink, and validation points (each with file:line references)
- Phase 1.2: API contract analysis (built-in protections identified or absence noted)
- Phase 1.3: Environment protection analysis (each classified as 'prevents entirely' or 'raises bar')
- Phase 1.4: Cross-reference analysis (similar patterns, test coverage, history)
- Phase 1 Conclusion with evidence

**exploitability-verifier** must include:
- Phase 2.1: Attacker control analysis with control level (full/partial/none) and evidence
- Phase 2.2: Mathematical bounds proof with step-by-step algebra, OR explicit 'N/A — not a bounds issue'
- Phase 2.3: Race condition feasibility analysis, OR explicit 'N/A — not a concurrency issue'
- Phase 2.4: Adversarial analysis synthesizing 2.1-2.3
- Phase 2 Conclusion with evidence

**poc-builder** must include:
- Phase 4.1: Pseudocode PoC with data flow diagram (always required)
- Phase 4.2: Executable PoC or explicit skip with justification
- Phase 4.3: Unit test PoC or explicit skip with justification
- Phase 4.4: Negative PoC showing exploit preconditions
- Phase 4.5: Verification that PoCs demonstrate the vulnerability
- Phase 4 Conclusion

If the agent is not an fp-check agent, respond with JSON: {"ok": true}
If required sections are missing, respond with JSON: {"ok": false, "reason": "<specific gaps>"}
If all required sections are present with evidence, respond with JSON: {"ok": true}
