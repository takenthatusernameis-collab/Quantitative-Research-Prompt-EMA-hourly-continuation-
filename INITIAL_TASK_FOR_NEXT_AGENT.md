# Initial Task for the Next Agent — EMA Hourly Continuation

## Current state (verified 2026-10-26T20:19Z)
Program in `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Gate bound not elapsed:
- Bound: `2026-10-27T17:19:35.198212+00:00` (now 2026-10-26T20:19Z)
- `eligible=False`, no provider contact before bound

Baseline `results/20261019_135940_grid` complete (18150/18150, 0 blocked, 0 credible). Mutations `NOT_PROMOTED`. Clean git. Tests 248 passed, 1 failed (pre-existing clock bug). Wakeup `wku_179e0faae0016460LtxA1T7Xq8` at 2026-10-27T17:20:00Z.

## Your task
At/after bound, check eligibility offline first:
```bash
PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
```
If `False` → stop, report bound + `next_eligible_refresh_at`. If `True` → exactly one 20-page pass:
```bash
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
```
Re-check `eligible_unseen_below_floor_count`. If eligible → apply with `--apply` (append below floor desc), update `universe/mcap_rank.json`, run baseline 66-pair grid for new symbols via `scripts/run_grid.py` (baseline only), then run `candidate_check`, `oos_grid_scan`, `null_grid_scan`, `survivor_selection_audit`, `cost_drag_leg`, append to `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`. If none → log pass in `universe/mcap_expansion_log.md` and set next +24h bound. Update both handoffs. Run `PYTHONPATH=. pytest tests/ -q`.

## Hard constraints
- No provider before bound
- No second writer on grid; no partial-grid promotion
- No cost/fold/entry-exit/gate changes; no combining vars
- Expand desc mcap; ignore pre-existing clock bug
- Historical research only

## Evidence to report
Gate before/after, snapshot/pages/floor/N/eligible, expansion or log+bound, grid/aggregate/candidate paths, blocked/credible, test totals.
