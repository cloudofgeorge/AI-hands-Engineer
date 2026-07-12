#!/usr/bin/env python3
"""Structural contract for the agent-neutral Kubernetes troubleshooting skill."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[6]
SKILL = ROOT / "skills/engineering/domains/infrastructure/troubleshooting-kubernetes/SKILL.md"
README = ROOT / "skills/engineering/README.md"
SKILLS_INDEX = ROOT / "skills/README.md"


def require(text: str, pattern: str, label: str) -> None:
    if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
        raise AssertionError(f"missing {label}: /{pattern}/")


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    require(text, r"^---\nname: troubleshooting-kubernetes\n", "agent-neutral name")
    require(text, r"^description: Use when", "trigger-oriented description")
    if re.search(r"\b(claude|anthropic)\b", text, flags=re.IGNORECASE):
        raise AssertionError("skill must not name a vendor-specific agent")

    for pattern, label in [
        (r"kubectl config current-context", "context discovery"),
        (r"auth can-i list pods", "list permission check"),
        (r"read-only", "read-only-first rule"),
        (r"explicit (?:user|operator) confirmation", "mutation approval gate"),
        (r"CrashLoopBackOff", "CrashLoopBackOff playbook"),
        (r"Pending", "Pending playbook"),
        (r"Service", "service troubleshooting path"),
        (r"NetworkPolic", "NetworkPolicy guardrail"),
        (r"helm status", "read-only Helm diagnostic"),
        (r"rollout undo.*--dry-run=server", "dry-run rollback preview"),
        (r"kubernetes\.io/docs", "official documentation link"),
    ]:
        require(text, pattern, label)

    readme = README.read_text(encoding="utf-8")
    require(
        readme,
        r"\[troubleshooting-kubernetes\]\(\./domains/infrastructure/troubleshooting-kubernetes/SKILL\.md\)",
        "engineering routing entry",
    )

    skills_index = SKILLS_INDEX.read_text(encoding="utf-8")
    count_match = re.search(
        r"\[Engineering\]\(\./engineering/README\.md\) \| (\d+) \|",
        skills_index,
    )
    if not count_match:
        raise AssertionError("missing Engineering count in top-level skills index")
    actual_count = sum(1 for _ in (ROOT / "skills/engineering").rglob("SKILL.md"))
    if int(count_match.group(1)) != actual_count:
        raise AssertionError(
            f"top-level Engineering count is {count_match.group(1)}, expected {actual_count}"
        )


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, FileNotFoundError) as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    print("PASS: Kubernetes troubleshooting skill contract")
