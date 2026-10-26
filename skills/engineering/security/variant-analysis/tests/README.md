# Variant-analysis fixture checks

The fixtures, expected results, and scoring helpers support offline verification of search and reporting behavior. The host-specific model evaluation launcher has been removed.

Run `bash run_fixtures.sh` from this directory to validate fixture integrity and run the grader and aggregator self-checks. It requires `uv`. No model service or plugin runtime is called.

These checks test fixtures and scoring logic; they do not establish the quality of an agent's vulnerability analysis.
