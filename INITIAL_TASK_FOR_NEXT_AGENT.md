# INITIAL TASK FOR NEXT AGENT

Gate NOT yet eligible (bound 2026-10-31T23:06:34.318029+00:00; now ~2026-10-31T13:38Z, ~9.5h remaining). Do NOT call provider.

## Verification performed at 2026-10-31T13:38:02Z

- `universe/last_scan.json` reconciles with `mcap_snapshot_20261030_230634.json`: scanned_at == fetched_at 2026-10-30T23:06:34.318029+00:00, coverage 20/20 pages (all_requested_pages_returned=true), entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3217157, universe_n=275 == mcap_rank.json n_symbols==len(symbols)==275, coverage_reaches_below_floor=true.
- Expansion floor ALEX/USDT $3,255,070 at snapshot rank 1986 confirmed (kucoin_usdt_pair=true, exclusion_reason=null). Below-floor band ranks 1987-2000: 14 entries all excluded (12 by `no_tradable_kucoin_spot_usdt_pair`, 2 by `insufficient_hourly_history_for_grid`: ALU rank 1999, MANYU rank 2000). eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[], state AWAITING_NEW_ELIGIBLE_CANDIDATES. next_eligible_refresh_at 2026-10-31T23:06:34.318029+00:00.
- Offline gate check (`scripts/refresh_gate.gate_status`): **not eligible** (bound 2026-10-31T23:06:34.318029+00:00 not elapsed, ~9.5h remaining; now 2026-10-31T13:38:02Z). No provider contact, no snapshot written, `last_scan.json` unchanged.
- Resume wakeup `wku_1919004cf001gDcjYnMequ1VV2` due ~2026-10-31T23:07:27.162Z exists; do not duplicate.
- No changes made; working tree clean (`git status --short` empty, `git diff --stat` empty).

## At/after the bound (2026-10-31T23:06:34.318029+00:00)

1. Offline gate check first (`scripts/refresh_gate.gate_status`).
2. If eligible: run at most one 20-page pass (`scripts/fetch_mcap_snapshot.py --pages 20`), recompute floor, inspect below-floor band, update `universe/last_scan.json`.
3. Do not call provider before bound; at most 1 pass/cycle; no changes to grid/costs/fills/history requirements; no grid reruns, no candle fetches.
4. Keep strict confirmatory separate from exploratory.
" filePath">
/home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-/INITIAL_TASK_FOR_NEXT_AGENT.md