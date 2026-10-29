# NEXT AGENT TASK

## Current state (2026-10-29T15:34:24Z)

- Gate status: **NOT ELIGIBLE** — 24h refresh bound `2026-10-29T21:24:11.948264+00:00` has not elapsed (now `2026-10-29T15:34:24.184208+00:00`, ~6h 0m remaining).
- Command run (this cycle): `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`
- Result: `{'eligible': False, 'bound': '2026-10-29T21:24:11.948264+00:00', 'now': '2026-10-29T15:34:24.184208+00:00', 'reason': 'the 24 h refresh bound 2026-10-29T21:24:11.948264+00:00 has not elapsed yet'}`
- Action taken: **stopped before any provider call**; re-set wakeup to `2026-10-29T21:41:37Z` (id `wku_1884e549c001wWrVVGaatBO5ay`). Single allowed wakeup; no second one created. Prior pending wakeups: none.
- Universe state unchanged: snapshot `mcap_snapshot_20261028_212411`, N=275, floor ALPINE/USDT $3,472,967, `eligible_unseen_below_floor_count` = 0, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`.
- Baseline grid: complete, 18150 cells, 0 credible. Child mutation `C_min_risk_atr` complete but not promoted.

## Measurable next task

At/after `2026-10-29T21:24:11.948264+00:00`, re-run the offline gate check:
```bash
PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
```
If still not eligible, stop and re-set the wakeup (do **NOT** call the provider). If eligible, run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`, recompute the expansion floor, and inspect the band strictly below the floor for `eligible_unseen_below_floor_count`. If 0, record the pass, set `next_eligible_refresh_at`, re-set the wakeup, and stop. If >0, expand per PROMPT.md §2.1 and run the full 66-pair grid on each new symbol via `scripts/run_grid.py`, then re-aggregate.

## Constraints (unchanged)

Historical research only; no orders/live/paper trading; no provider before bound; 1 pass max/cycle; do not fetch new candle data; do not modify baseline grid/costs/fills/entry-exit semantics; do not trigger/cancel/rerun GitHub Actions or edit workflows; do not create a second wakeup; keep strict confirmatory separate from exploratory.