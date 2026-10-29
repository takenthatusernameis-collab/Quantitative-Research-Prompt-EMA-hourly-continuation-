# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-29T01:12Z)
- Gate checked **offline** at 2026-10-29T01:12:15.115975+00:00: **eligible=False** (bound
  2026-10-29T21:24:11.948264+00:00 not yet elapsed; ~20h12m remaining). No provider contact made.
  Task complete: nothing actionable before the bound; wakeup already scheduled, not re-scheduled.
- Scan: 20-page pass `mcap_snapshot_20261028_212411` (2000 entries, 20/20 pages,
  history_probe_failures=0). Coverage reaches below expansion floor;
  eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411;
  batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor ALPINE/USDT $3,472,967.
- next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Wakeup: **wku_18537a5210016Rc5AsWtWz414P**, due 2026-10-29T21:21:48Z (just before bound; gate check first).
  Single resume wakeup already scheduled. Do **not** re-schedule a duplicate.
- Baseline grid `results/20261019_135940_grid` re-verified: summary.json n_cells 18150,
  n_symbols 275, n_pairs 66, mean net PF 0.4987; progress.json all_symbols_processed=true,
  next_cell=null, stopped=false, stop_reason=null, completed_cells=18150, 0 blocked,
  0 credible candidates.

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

(End of file - total 35 lines)