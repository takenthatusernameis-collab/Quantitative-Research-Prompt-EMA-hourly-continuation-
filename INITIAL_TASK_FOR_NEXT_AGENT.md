# Initial task for the next agent — single-variable mutation of expanded baseline

## Situation (verified 2026-10-22T13:20Z)

Expanded universe complete: N=275, grid 18150/18150 cells (0 blocked). Aggregate done: mean net PF 0.4987, 37 cells net PF>1, candidate_check rejected all. Tests 249 passed. State AWAITING_NEW_ELIGIBLE_CANDIDATES. Next eligible refresh 2026-10-23T12:15:58Z.

## Task

Run a new single-variable mutation of the expanded baseline (not ATR filter, which stays closed) using scripts/run_mutation_grid.py single-variable flags (--stricter-trend, --min-risk-atr, --atr-threshold, --rr, --aggressive-exit), keeping registered costs, folds, entry/exit semantics and §3.4 gates unchanged, evaluated against the child's own randomized null. Mutate one variable at a time.

## Must not

No provider contact before 2026-10-23T12:15:58Z. No re-run baseline grid. No change to registered grid/cost model/fill rule/folds/gates.
