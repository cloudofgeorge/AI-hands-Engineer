#!/usr/bin/env bash
# Offline fixture integrity and scoring checks; no host-specific model runtime.

set -euo pipefail

command -v uv >/dev/null 2>&1 || {
  echo "uv is required (https://docs.astral.sh/uv/)" >&2
  exit 1
}

TESTS_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "→ variant-analysis fixtures"
uv run --no-project "$TESTS_DIR/verify_fixtures.py"

echo "→ grader self-test"
uv run --no-project "$TESTS_DIR/score.py" --self-test

echo "→ aggregator self-test"
uv run --no-project "$TESTS_DIR/summarize.py" --self-test
