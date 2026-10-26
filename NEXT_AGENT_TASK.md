# NEXT AGENT TASK — Durable Handoff

## Turn 2026-10-26T21:05Z (this turn, wakeup waiting for bound)
- Gate bound: `2026-10-27T17:19:35.198212+00:00` NOT yet elapsed (now 2026-10-26T21:05Z).
- Offline `gate_status` verified: `eligible=False`, reason "the 24 h refresh bound ... has not elapsed yet".
- No provider contact before bound (honored). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261026_171935`, N=275, floor `ALPINE/USDT` $3,426,968.
- Baseline grid `results/20261019_135940_grid` complete (18150/18150, 0 blocked, 0 credible candidates). Child grids documented `NOT_PROMOTED` in `results/mutations.json`.
- `git status` clean. Full test suite: **248 passed, 1 failed** (pre-existing clock bug in `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`; ignore per constraints).
- Wakeup scheduled: `wku_179e0faae0016460LtxA1T7Xq8` at 2026-10-27T17:20:00Z.

## Next action (after bound)
```bash
PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
```
If `eligible=False` → stop, report bound + `next_eligible_refresh_at`. If `eligible=True` → run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`, re-check `eligible_unseen_below_floor_count`. If eligible exist → apply with `--apply` (append below floor in desc mcap), update `universe/mcap_rank.json`, run baseline 66-pair grid via `scripts/run_grid.py` for new symbols only or full if needed per implementation (baseline config only; no cost/fold/entry-exit/gate changes; no combining vars), then run `candidate_check`, `oos_grid_scan`, `null_grid_scan`, `survivor_selection_audit`, `cost_drag_leg`, append to `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`. If none → record pass in `universe/mcap_expansion_log.md` and set next +24h bound.

## Constraints
- No provider before bound; no second writer on grid; no partial-grid promotion; no changes to costs/folds/entry-exit/gates; don't combine vars; expand desc mcap; ignore pre-existing clock bug.
- Historical research only.

## Evidence to report
Gate before/after, snapshot path/pages/floor/N/eligible, expansion details or log+bound, grid/aggregate/candidate paths, blocked/credible, tests.
