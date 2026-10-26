# Initial Task for the Next Agent — EMA Hourly Continuation

## Current state (verified 2026-10-26T20:07Z)

The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES`. The market-cap ranking
refresh is gated by a 24 h bound (PROMPT.md §2.1.5) that has **not** elapsed:

- Bound: `2026-10-27T17:19:35.198212+00:00` (current time 2026-10-26T20:11Z)
- Gate check: `eligible=False`
- No provider contact is permitted before the bound elapses.

Baseline grid `results/20261019_135940_grid` is complete and verified
(18 150/18 150 cells, 275 symbols × 66 EMA pairs, 0 blocked, 0 credible
candidates). Both child mutation grids are complete and documented as
`NOT_PROMOTED` in `results/mutations.json`. `git status` is clean.

## Your task

Wait for the gate bound to elapse, then check eligibility offline first
(no provider contact before this returns `eligible: True`):

```bash
PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
```

If `eligible: False`, stop and report the bound and
`next_eligible_refresh_at`; do not contact the provider.

If `eligible: True`, run exactly one 20-page ranking pass:

```bash
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
```

Then re-check `eligible_unseen_below_floor_count` from
`universe/last_scan.json`:

- **If eligible names exist:** apply with `--apply` (append in descending
  market-cap order, strictly below the floor), update
  `universe/mcap_rank.json`, and re-run the full 66-pair EMA grid for each
  newly added symbol through `scripts/run_grid.py` (baseline config only —
  do not change costs, folds, entry/exit, or gates; do not combine
  variables). Then run the standard legs (`candidate_check`,
  `oos_grid_scan`, `null_grid_scan`, `survivor_selection_audit`,
  `cost_drag_leg`) on the expanded grid and append to
  `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`. Preserve
  all negative and blocked results; do not promote any candidate without
  auditable net-of-cost out-of-sample evidence.
- **If no eligible names:** record the pass in
  `universe/mcap_expansion_log.md` and set the next +24 h bound.

Finally, update both handoff files (`NEXT_AGENT_TASK.md` and this file) with
gate status before/after, snapshot path/pages/floor/N and eligible count,
grid paths and blocked/credible counts, and the next bound; then run the
test suite (`PYTHONPATH=. pytest tests/ -q`) and report totals.

## Hard constraints

- No provider call before the recorded bound has elapsed.
- No second writer on a grid in progress; no partial-grid promotion.
- No changes to costs, folds, entry/exit semantics, or acceptance gates.
- Do not combine variables; do not stop on failures — expand descending
  market cap and continue.
- Ignore the pre-existing clock bug in
  `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`.
- Never place orders or deploy live/paper trading. Historical research only.

## Evidence to report

Gate status before/after; snapshot path/pages/floor/N and eligible count; if
expanded, old→new N, ranks, and log entry; if not, log entry + new bound;
grid/aggregate/candidate paths and blocked/credible counts; test totals after
changes (or confirmation that nothing changed).