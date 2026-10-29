# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-29T07:24Z)
- Gate checked offline: eligible=False (bound 2026-10-29T21:24:11.948264+00:00 not yet elapsed; ~13h39m remaining at 2026-10-29T07:24Z). No provider contact made. Verified via `scripts.refresh_gate.gate_status` at `2026-10-29T07:24:40.933959+00:00`.
- Wakeup: a single resume wakeup (wku_18644a6b2001tKcU6d6A3PdIWy) is set for 2026-10-29T21:29:00Z, just after the bound. Do NOT create a second one; let it fire (cross-session, may not appear in `cron_list` of this session).
- Last scan: mcap_snapshot_20261028_212411 (2000 entries, 20/20 pages). eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor: ALPINE/USDT at $3,472,967; next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Baseline grid results/20261019_135940_grid re-verified: summary.json n_cells=18150, n_symbols=275, n_pairs=66, 0 credible candidates (n_exploratory_signal=27, n_rejected=18123, n_blocked=0); progress.json all_symbols_processed=true, next_cell=null, stopped=false, stop_reason=null, completed_cells=18150, 0 blocked.
- Recompute floor from fresh snapshot at pass time — do not assume values without recomputing.
- Git status clean; no uncommitted changes.

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
