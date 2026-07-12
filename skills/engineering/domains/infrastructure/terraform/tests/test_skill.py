#!/usr/bin/env python3
"""Structural contract for the agent-neutral Terraform safety skill."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[6]
SKILL = ROOT / "skills/engineering/domains/infrastructure/terraform/SKILL.md"
README = ROOT / "skills/engineering/README.md"
SKILLS_INDEX = ROOT / "skills/README.md"


def require(text: str, pattern: str, label: str) -> None:
    if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
        raise AssertionError(f"missing {label}: /{pattern}/")


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    require(text, r"^---\nname: terraform\n", "agent-neutral name")
    require(text, r"^description: Use when", "trigger-oriented description")
    if re.search(r"\b(claude|anthropic)\b", text, flags=re.IGNORECASE):
        raise AssertionError("skill must not name a vendor-specific agent")
    if re.search(r"terraform\s+(?:apply|destroy)\b[^\n]*-auto-approve", text, flags=re.IGNORECASE):
        raise AssertionError("skill must not normalize auto-approved mutation")

    for pattern, label in [
        (r"terraform version", "CLI identity check"),
        (r"terraform workspace show", "workspace discovery"),
        (r"terraform init -backend=false", "offline validation initialization"),
        (r"terraform fmt -check", "format validation"),
        (r"terraform validate", "configuration validation"),
        (r"terraform plan", "plan-first workflow"),
        (r"-refresh-only", "refresh-only diagnosis path"),
        (r"force-unlock", "state-lock guardrail"),
        (r"read-only", "read-only-first rule"),
        (r"explicit (?:user|operator)(?:\s+or\s+(?:user|operator))? confirmation", "mutation approval gate"),
        (r"backend", "backend boundary"),
        (r"developer\.hashicorp\.com/terraform", "official documentation link"),
    ]:
        require(text, pattern, label)

    readme = README.read_text(encoding="utf-8")
    require(
        readme,
        r"\[terraform\]\(\./domains/infrastructure/terraform/SKILL\.md\)",
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
    print("PASS: Terraform safety skill contract")
