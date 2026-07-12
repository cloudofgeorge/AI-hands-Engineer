#!/usr/bin/env python3
"""Structural contract for the agent-neutral CI/CD safety skill."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[5]
SKILL = ROOT / "skills/engineering/tools/ci-cd/SKILL.md"
README = ROOT / "skills/engineering/README.md"
SKILLS_INDEX = ROOT / "skills/README.md"


def require(text: str, pattern: str, label: str) -> None:
    if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
        raise AssertionError(f"missing {label}: /{pattern}/")


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    require(text, r"^---\nname: ci-cd\n", "agent-neutral name")
    require(text, r"^description: Use when", "trigger-oriented description")
    if re.search(r"\b(claude|anthropic)\b", text, flags=re.IGNORECASE):
        raise AssertionError("skill must not name a vendor-specific agent")

    for pattern, label in [
        (r"read-only", "read-only-first rule"),
        (r"explicit (?:user|operator)(?:\s+or\s+(?:user|operator))? confirmation", "mutation approval gate"),
        (r"least privilege", "least-privilege permissions"),
        (r"full-length commit SHA", "immutable action pinning"),
        (r"pull_request_target", "untrusted pull-request guardrail"),
        (r"OIDC", "credential guidance"),
        (r"artifact", "artifact identity guidance"),
        (r"rollback", "rollback requirement"),
        (r"GitLab", "GitLab scope"),
        (r"rules", "GitLab rules guidance"),
        (r"docs\.github\.com", "official GitHub documentation link"),
    ]:
        require(text, pattern, label)

    readme = README.read_text(encoding="utf-8")
    require(
        readme,
        r"\[ci-cd\]\(\./tools/ci-cd/SKILL\.md\)",
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
    print("PASS: CI/CD safety skill contract")
