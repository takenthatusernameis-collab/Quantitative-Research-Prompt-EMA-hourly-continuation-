# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-29T07:13Z)
- Gate checked offline: eligible=False (bound 2026-10-29T21:24:11.948264+00:00 not yet elapsed; ~14h11m remaining). No provider contact made. Verified via `scripts.refresh_gate.gate_status` at `2026-10-29T07:13:11.051137+00:00`.
- Wakeup: a single resume wakeup (wku_18644a6b2001tKcU6d6A3PdIWy) is set for 2026-10-29T21:29:00Z, just after the bound. Do NOT create a second one; let it fire (cross-session, may not appear in `cron_list` of this session).
- Last scan: mcap_snapshot_20261028_212411 (2000 entries, 20/20 pages). eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor: ALPINE/USDT at $3,472,967; next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Baseline grid results/20261019_135940_grid re-verified: summary.json n_cells=18150, n_symbols=275, n_pairs=66, 0 credible candidates; progress.json all_symbols_processed=true, next_cell=null, stopped=false, stop_reason=null, completed_cells=18150, 0 blocked.
- Recompute floor from fresh snapshot at pass time — do not assume values without recomputing.
- Git status clean; no uncommitted changes.

## Verification performed this turn (2026-10-29T07:13Z, all offline, no provider contact)
- `gate_status(universe/last_scan.json)` → `{'eligible': False, 'bound': '2026-10-29T21:24:11.948264+00:00', 'now': '2026-10-29T07:13:11.051137+00:00', 'reason': 'the 24 h refresh bound ... has not elapsed yet'}`.
- Snapshot `universe/mcap_snapshot_20261028_212411.json` re-read directly: fetched_at 2026-10-28T21:24:11.948264+00:00, len(entries)=2000, pages_fetched=20, pages_requested=20, all_requested_pages_returned=True, lowest_rank_covered=2000, lowest_market_cap_usd=3410633, history_probe_failure_count=0. Floor ALPINE/USDT $3,472,967 sits above the lowest observed mcap, so the band below the floor was observed by this pass.
- `universe/last_scan.json` re-read directly: state AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[], next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00 — unchanged.
- Baseline grid re-verified complete: `results/20261019_135940_grid/progress.json` completed_cells=18150, n_symbols=275, n_pairs=66, all_symbols_processed=True, next_cell=None, stopped=False, stop_reason=None, "blocked" substring count 0; `summary.json` pooled mean net PF 0.4987, median 0.5198, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_rejected 18123, n_blocked 0, **0 credible candidates**.
- Script imports all OK: scripts.refresh_gate, scripts.fetch_mcap_snapshot, scripts.fetch_kucoin, scripts.run_grid, scripts.aggregate_grid, scripts.candidate_check, scripts.refresh_universe.
- `git status --short` empty, `git diff --stat` empty — working tree clean.

## Next action at/after bound
At/after 2026-10-29T21:24:11.948264+00:00:
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, stop (no provider); re-set wakeup per interval policy.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor; inspect band strictly below floor.
4. If count==0: record pass, set next bound, re-set wakeup, stop.
5. If count>0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol.
6. Update both handoffs with evidence (snapshot_id, counts, results paths) and preserve negative/blocked results.

## Constraints
- No provider before bound; historical research only.
- One 20-page pass max per cycle.
- Do not trigger/cancel/rerun/dispatch GitHub Actions.
- Do not fetch new candle data; do not modify baseline grid or costs/fills/entry-exit.
- Preserve all negative/blocked results.