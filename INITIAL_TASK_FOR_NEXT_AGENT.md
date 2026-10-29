# Initial Task For Next Agent

Read `NEXT_AGENT_TASK.md` first.

## Situation
Gate bound 2026-10-29T21:24:11.948264+00:00 has NOT elapsed (re-verified 2026-10-29T07:13:11Z: eligible=False, ~14h11m remaining via `scripts.refresh_gate.gate_status`). Do NOT contact the provider before the bound. A single resume wakeup (wku_18644a6b2001tKcU6d6A3PdIWy) is set for 2026-10-29T21:29:00Z — let it fire; do NOT duplicate or reschedule it.

## Verification performed this turn (2026-10-29T07:13Z, all offline, no provider contact)
- Gate: `eligible=False`, bound 2026-10-29T21:24:11.948264+00:00, now 2026-10-29T07:13:11.051137+00:00.
- Snapshot `universe/mcap_snapshot_20261028_212411.json`: fetched_at 2026-10-28T21:24:11.948264+00:00, 2000 entries, 20/20 pages, all_requested_pages_returned=True, lowest_market_cap_usd 3410633, history_probe_failure_count=0. Floor ALPINE/USDT $3,472,967 is above the lowest observed mcap → band below floor was observed.
- `universe/last_scan.json`: state AWAITING_NEW_ELIGIBLE_CANDIDATES, eligible_unseen_below_floor_count=0, batch_selected=[], next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00 — unchanged.
- Baseline grid `results/20261019_135940_grid`: completed_cells=18150, n_symbols=275, n_pairs=66, all_symbols_processed=True, next_cell=null, stopped=false, stop_reason=null, 0 blocked; pooled mean net PF 0.4987, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_rejected 18123, **0 credible candidates**.
- Script imports OK: refresh_gate, fetch_mcap_snapshot, fetch_kucoin, run_grid, aggregate_grid, candidate_check, refresh_universe.
- `git status --short` empty, `git diff --stat` empty — working tree clean.

## On wakeup (at/after bound)
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, stop (no provider); re-set wakeup per interval policy.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor from fresh snapshot; inspect band strictly below floor for eligible unseen candidates.
4. If count==0: record pass, set next bound, re-set wakeup, stop.
5. If count>0: expand per PROMPT.md §2.1 and run full 66-pair grid on each new symbol.
6. Update both handoffs with evidence (snapshot_id, counts, results paths) and preserve negative/blocked results.

## Hard constraints
No provider before bound; one pass max per cycle; no GitHub Actions; no new candle data; no changes to baseline grid/costs/fills/entry-exit; preserve negative/blocked results.
