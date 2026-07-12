#!/usr/bin/env python3
"""Structural contract for the agent-neutral AWS FinOps safety skill."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[6]
SKILL = ROOT / "skills/engineering/domains/infrastructure/aws-finops/SKILL.md"
README = ROOT / "skills/engineering/README.md"
SKILLS_INDEX = ROOT / "skills/README.md"


def require(text: str, pattern: str, label: str) -> None:
    if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
        raise AssertionError(f"missing {label}: /{pattern}/")


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    require(text, r"^---\nname: aws-finops\n", "agent-neutral name")
    require(text, r"^description: Use when", "trigger-oriented description")
    if re.search(r"\b(claude|anthropic)\b", text, flags=re.IGNORECASE):
        raise AssertionError("skill must not name a vendor-specific agent")

    for pattern, label in [
        (r"read-only", "read-only-first rule"),
        (r"explicit (?:user|operator)(?:\s+or\s+(?:user|operator))? confirmation", "mutation approval gate"),
        (r"aws sts get-caller-identity", "account identity check"),
        (r"aws ce get-cost-and-usage", "Cost Explorer read command"),
        (r"estimated", "billing-data uncertainty"),
        (r"Cost and Usage Report", "CUR guidance"),
        (r"Budgets", "budget-change guardrail"),
        (r"Savings Plans|Reserved Instances", "commitment guardrail"),
        (r"least privilege", "IAM safety"),
        (r"rollback", "rollback requirement"),
        (r"docs\.aws\.amazon\.com", "official AWS documentation link"),
    ]:
        require(text, pattern, label)

    readme = README.read_text(encoding="utf-8")
    require(readme, r"\[aws-finops\]\(\./domains/infrastructure/aws-finops/SKILL\.md\)", "engineering routing entry")
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
    print("PASS: AWS FinOps safety skill contract")
