# INITIAL TASK FOR NEXT AGENT

Gate NOT yet eligible (bound 2026-10-31T23:06:34.318029+00:00). Do NOT call provider. Current time 2026-10-31T19:29:07Z.

## Verified state (2026-10-31T19:29:07Z)
- `universe/last_scan.json` matches `universe/mcap_snapshot_20261030_230634.json`: `scanned_at`==`fetched_at`==2026-10-30T23:06:34.318029+00:00; coverage 20/20 pages, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3217157, coverage_reaches_below_floor=true.
- Universe N=275 (`universe/mcap_rank.json` n_symbols==275, unique==275). Expansion floor ALEX/USDT (ALEX Lab) rank 1986 $3,255,070 with `kucoin_usdt_pair=true`/`exclusion_reason=null` (confirmed in snapshot).
- Below-floor band ranks 1987-2000 (14 entries): all excluded — 12 by `no_tradable_kucoin_spot_usdt_pair` (RMRVL/ASMLON/ALTSZN/TRIPLET/SN46/WAAC/CHECK/DDX/AMZN/PWEASE/金蝶圣甲/PNIC), 2 by `insufficient_hourly_history_for_grid` (ALU rank 1999, MANYU rank 2000).
- `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `next_eligible_refresh_at`=2026-10-31T23:06:34.318029+00:00.
- Grids reconciled complete (0 credible candidates). No snapshot written, no provider contact. `git status --short` clean. No pending wakeups for this session.

## Measurable next task
1. **Wait for gate**: At/after `2026-10-31T23:06:34.318029+00:00`, do an offline gate check (read `universe/last_scan.json` / `scripts/refresh_gate.py`). If bound not elapsed, do nothing except confirm state.
2. **If eligible and coverage allows**: Run at most one 20-page pass via `scripts/fetch_mcap_snapshot.py --pages 20` (respecting gate; use `--override-gate` only if explicitly justified per policy). After fetch, recompute floor against current universe, inspect below-floor band (ranks below floor), and update `universe/last_scan.json` via the script. Do **not** auto-apply expansion unless `--apply` is used and batch is reviewed.
3. **If still ineligible/no eligible unseen**: Confirm state, do not rerun full 275-symbol grid, do not fetch new candle data, do not change baseline grid/costs/fills/entry-exit semantics. Keep strict confirmatory separate from exploratory.
4. **Handoff discipline**: Preserve all negative/blocked results. If no eligible candidates found after a valid pass that reaches below floor, record state `AWAITING_NEW_ELIGIBLE_CANDIDATES` with updated `next_eligible_refresh_at` (script does this). Resume wakeup `wku_1919004cf001gDcjYnMequ1VV2` due ~2026-10-31T23:07:27.162Z owned by prior session if present; do not duplicate.

## Constraints
Historical research only; no orders/live/paper trading; no provider before bound; 1 pass max/cycle; no workflow changes; preserve all negative/blocked results.