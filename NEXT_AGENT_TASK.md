# NEXT AGENT TASK

## Current state (2026-10-29T19:16:00Z)

- Gate status: **NOT ELIGIBLE** — 24h refresh bound `2026-10-29T21:24:11.948264+00:00` has not elapsed (now `2026-10-29T19:15:21.726470+00:00`, ~2h 8m 49s remaining).
- Command run (this cycle): `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`
- Result: `{'eligible': False, 'bound': '2026-10-29T21:24:11.948264+00:00', 'now': '2026-10-29T19:15:21.726470+00:00', 'reason': 'the 24 h refresh bound 2026-10-29T21:24:11.948264+00:00 has not elapsed yet'}` (bound = scanned_at + 24h, scanned_at = 2026-10-28T21:24:11.948264+00:00).
- Action taken: **Stopped before any provider call.** Gate remains NOT ELIGIBLE. Offline gate check confirmed; `last_scan.json` unchanged.
- Wakeup discipline: single wakeup `wku_18918e4a3001gEIk8ezcAu2UAc` due `2026-10-29T21:25:00.000Z` (only pending wakeup). No second wakeup created.
- Universe state unchanged: snapshot `mcap_snapshot_20261028_212411`, N=275, floor ALPINE/USDT $3,472,967, `eligible_unseen_below_floor_count` = 0, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`.
- Baseline grid: complete (18150 cells), 0 credible candidates. Child mutation `C_min_risk_atr` complete but not promoted.
- Git status: clean (no uncommitted changes).

## Measurable next task

At/after `2026-10-29T21:25:00.000Z` (single wakeup `wku_18918e4a3001gEIk8ezcAu2UAc` already set), re-run the offline gate check:
```bash
PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
```
If still not eligible, stop and re-set a single wakeup just after the bound (do **NOT** call the provider). If eligible, run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`, recompute the expansion floor, and inspect the band strictly below the floor for `eligible_unseen_below_floor_count`. If 0, record the pass, set `next_eligible_refresh_at`, re-set the wakeup just after the new bound, and stop. If >0, expand per PROMPT.md §2.1 and run the full 66-pair grid on each new symbol via `scripts/run_grid.py`, then re-aggregate.

## Constraints (unchanged)

Historical research only; no orders/live/paper trading; no provider before bound; 1 pass max/cycle; do not fetch new candle data; do not modify baseline grid/costs/fills/entry-exit semantics; do not trigger/cancel/rerun GitHub Actions or edit workflows; single wakeup only; keep strict confirmatory separate from exploratory.