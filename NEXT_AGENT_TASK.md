# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-29T01:28Z)
- Gate re-checked offline at 2026-10-29T01:27:45Z: eligible=False (bound 2026-10-29T21:24:11.948264+00:00 not yet elapsed; ~20h remaining). No provider contact made. Confirmed via `scripts/refresh_gate.gate_status(universe/last_scan.json)`.
- Scan: 20-page pass mcap_snapshot_20261028_212411 (2000 entries, 20/20 pages, history_probe_failures=0). eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor ALPINE/USDT $3,472,967.
- next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Resume wakeup: wku_1854019a7001eMyiUzafmTDAOy, due 2026-10-29T21:21:48Z. Do not re-schedule a duplicate.
- Baseline grid results/20261019_135940_grid verified: n_cells 18150, n_symbols 275, n_pairs 66, mean net PF 0.4987; complete, 0 blocked, 0 credible candidates.

## Next action at/after bound
At/after 2026-10-29T21:24:11.948264+00:00:
1. Check gate offline. If not eligible, re-set wakeup and stop.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor; inspect band strictly below floor.
4. If count==0: record pass, set next bound, re-set wakeup, stop.
5. If count>0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol.
6. Update both handoffs.

## Constraints
- No provider before bound; historical research only.
- One 20-page pass max per cycle.
- Do not trigger/cancel/rerun/dispatch GitHub Actions.
- Do not fetch new candle data; do not modify baseline grid or costs/fills/entry-exit.
- Preserve all negative/blocked results.
"
