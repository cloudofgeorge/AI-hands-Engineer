#!/usr/bin/env python3
"""Structural contract for the agent-neutral GitOps safety skill."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[6]
SKILL = ROOT / "skills/engineering/domains/infrastructure/gitops/SKILL.md"
README = ROOT / "skills/engineering/README.md"
SKILLS_INDEX = ROOT / "skills/README.md"


def require(text: str, pattern: str, label: str) -> None:
    if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
        raise AssertionError(f"missing {label}: /{pattern}/")


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    require(text, r"^---\nname: gitops\n", "agent-neutral name")
    require(text, r"^description: Use when", "trigger-oriented description")
    if re.search(r"\b(claude|anthropic)\b", text, flags=re.IGNORECASE):
        raise AssertionError("skill must not name a vendor-specific agent")

    for pattern, label in [
        (r"read-only", "read-only-first rule"),
        (r"explicit (?:user|operator)(?:\s+or\s+(?:user|operator))? confirmation", "mutation approval gate"),
        (r"argocd app diff", "Argo CD diff command"),
        (r"flux get kustomizations", "Flux inspection command"),
        (r"-n \"\$NAMESPACE\"", "namespace-scoped Flux inspection"),
        (r"reconcile", "reconciliation guardrail"),
        (r"prune", "prune guardrail"),
        (r"rollback", "rollback requirement"),
        (r"manual.*kubectl", "manual-live-change guardrail"),
        (r"Secret", "secret handling"),
        (r"argo-cd\.readthedocs\.io|fluxcd\.io", "official documentation link"),
        (r"flux_reconcile_kustomization", "canonical Flux reconcile documentation link"),
    ]:
        require(text, pattern, label)
    if re.search(r"^flux get .*\s-A\s*$", text, flags=re.IGNORECASE | re.MULTILINE):
        raise AssertionError("Flux read-only examples must not default to all-namespaces enumeration")

    readme = README.read_text(encoding="utf-8")
    require(readme, r"\[gitops\]\(\./domains/infrastructure/gitops/SKILL\.md\)", "engineering routing entry")
    count_match = re.search(r"\[Engineering\]\(\./engineering/README\.md\) \| (\d+) \|", SKILLS_INDEX.read_text())
    if not count_match:
        raise AssertionError("missing Engineering count in top-level skills index")
    actual_count = sum(1 for _ in (ROOT / "skills/engineering").rglob("SKILL.md"))
    if int(count_match.group(1)) != actual_count:
        raise AssertionError(f"top-level Engineering count is {count_match.group(1)}, expected {actual_count}")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, FileNotFoundError) as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    print("PASS: GitOps safety skill contract")
