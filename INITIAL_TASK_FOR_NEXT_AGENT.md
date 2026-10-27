# Initial Task for the Next Agent — EMA Hourly Continuation

## Current state (verified 2026-10-27T00:27Z)
Program in `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Gate bound not elapsed:
- Bound: `2026-10-27T17:19:35.198212+00:00` (now 2026-10-27T00:27:51+00:00`)
- `eligible=False` (offline gate_status), no provider contact before bound

Baseline `results/20261019_135940_grid` complete (18150/18150, 0 blocked, 0 credible). Mutations `NOT_PROMOTED`. Clean git. Tests 248 passed, 1 failed (pre-existing clock bug in `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`; ignore).

## Your task
At/after bound, check eligibility offline first:
```bash
PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
```
If `False` → stop, report bound + reason. If `True` → exactly one 20-page pass:
```bash
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
```
Re-check `eligible_unseen_below_floor_count`. If >0 → apply with `--apply` (append below floor desc), update `universe/mcap_rank.json`, run baseline 66-pair grid for new symbols only or full per implementation (baseline only), then run `candidate_check`, `oos_grid_scan`, `null_grid_scan`, `survivor_selection_audit`, `cost_drag_leg`, append to `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`. If 0 → log in `universe/mcap_expansion_log.md` and set next +24h bound. Update both handoffs. Run `PYTHONPATH=. python3 -m pytest tests/ -q`.

## Hard constraints
- No provider before bound; no second writer on grid; no partial-grid promotion
- No cost/fold/entry-exit/gate changes; no combining vars
- Expand desc mcap; ignore pre-existing clock bug
- Historical research only

## Update 2026-10-27T00:27Z (current)
Gate re-checked offline at now `2026-10-27T00:27:51.439276+00:00`: `eligible=False`, reason "the 24 h refresh bound 2026-10-27T17:19:35.198212+00:00 has not elapsed yet". Bound unchanged. No provider contact (compliant). Wakeup `wku_17ac1d952001heirgJXXJsOaEZ` at 2026-10-27T17:20:00Z remains scheduled (single). Baseline grid complete (18150/18150, 0 blocked, 0 credible). Mutations `NOT_PROMOTED`. Git clean. `last_scan.json` unchanged (N=275, floor `ALPINE/USDT` $3,426,968, eligible_unseen_below_floor_count=0). Nothing actionable before bound.

**Clear initial task message for next agent:** At/after bound `2026-10-27T17:19:35.198212+00:00`, check eligibility offline first with `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"`. If `eligible=False` → stop and report bound + reason. If `eligible=True` → run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`. Re-check `eligible_unseen_below_floor_count`. If >0 → apply with `--apply` (append below floor in desc mcap order), update `universe/mcap_rank.json`, run baseline 66-pair grid for new symbols only or full per implementation (baseline config only; no cost/fold/entry-exit/gate changes; no combining vars), then run `candidate_check`, `oos_grid_scan`, `null_grid_scan`, `survivor_selection_audit`, `cost_drag_leg`, append to `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`. If 0 → record pass in `universe/mcap_expansion_log.md` and set next +24h bound via gated refresh path. Update both handoffs. Run `PYTHONPATH=. python3 -m pytest tests/ -q`. Constraints: no provider before bound, no second writer on grid, no partial-grid promotion, no changes to costs/folds/entry-exit/gates, expand desc mcap only, historical research only, ignore pre-existing clock bug.

## Evidence to report
Gate before/after, snapshot/pages/floor/N/eligible, expansion or log+bound, grid/aggregate/candidate paths, blocked/credible, test totals.
## Update 2026-10-27T00:32Z (current)
Gate re-checked offline at now `2026-10-27T00:32:45.527672+00:00`: `eligible=False`, reason "the 24 h refresh bound 2026-10-27T17:19:35.198212+00:00 has not elapsed yet". Bound unchanged. No provider contact (compliant). Wakeup `wku_17abec669001vODhASpL0ihrmJ` at 2026-10-27T17:20:00Z remains scheduled (single). Baseline grid complete (18150/18150, 0 blocked, 0 credible). Mutations `NOT_PROMOTED`. Git clean. `last_scan.json` unchanged (N=275, floor `ALPINE/USDT` $3,426,968, eligible_unseen_below_floor_count=0). Nothing actionable before bound. Handoffs updated.

**Clear initial task message for next agent:** At/after bound `2026-10-27T17:19:35.198212+00:00`, check eligibility offline first with `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"`. If `eligible=False` → stop and report bound + reason. If `eligible=True` → run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`. Re-check `eligible_unseen_below_floor_count`. If >0 → apply with `--apply` (append below floor in desc mcap order), update `universe/mcap_rank.json`, run baseline 66-pair grid for new symbols only or full per implementation (baseline config only; no cost/fold/entry-exit/gate changes; no combining vars), then run `candidate_check`, `oos_grid_scan`, `null_grid_scan`, `survivor_selection_audit`, `cost_drag_leg`, append to `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`. If 0 → record pass in `universe/mcap_expansion_log.md` and set next +24h bound via gated refresh path. Update both handoffs. Run `PYTHONPATH=. python3 -m pytest tests/ -q`. Constraints: no provider before bound, no second writer on grid, no partial-grid promotion, no changes to costs/folds/entry-exit/gates, expand desc mcap only, historical research only, ignore pre-existing clock bug.
