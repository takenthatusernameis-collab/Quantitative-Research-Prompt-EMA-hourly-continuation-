# INITIAL TASK FOR NEXT AGENT — Durable Handoff

## Task
Resume the gated market-cap expansion cycle for the EMA hourly continuation research program. Read `README.md`, `AGENTS.md`, `PROMPT.md`, and `NEXT_AGENT_TASK.md` first.

## Current state (turn 2026-10-29T08:30Z)
- Gate re-checked offline this turn: eligible=False. Bound 2026-10-29T21:24:11.948264+00:00 has not elapsed yet (~12h53m remaining). No provider contact made. Verified via `scripts.refresh_gate.gate_status` — `{'eligible': False, 'bound': '2026-10-29T21:24:11.948264+00:00', 'now': '2026-10-29T08:30:52.841139+00:00', 'reason': 'the 24 h refresh bound 2026-10-29T21:24:11.948264+00:00 has not elapsed yet'}`. Prior task completed as blocked-on-gate; no expansion performed.
- Wakeup: a single resume wakeup (wku_18644a6b2001tKcU6d6A3PdIWy) is set for 2026-10-29T21:29:00Z, just after the bound. `cancel_wakeup list` in this session returned no pending wakeups (cross-session visibility). Do NOT create a second one; let it fire.
- Last scan: mcap_snapshot_20261028_212411 (2000 entries, 20/20 pages, fetched_at 2026-10-28T21:24:11.948264+00:00, lowest rank 2000, lowest mcap $3,410,633). eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor recomputed from the snapshot: ALPINE/USDT at $3,472,967; next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Baseline grid results/20261019_135940_grid re-verified:
  - summary.json.pooled: n_cells=18150, n_symbols=275, n_pairs=66, total_trades=14676563, mean_net_pf=0.4987, median_net_pf=0.5198, best_net_pf=2.2274, n_cells_net_pf_gt_1=37, n_exploratory_signal=27, n_rejected=18123, n_blocked=0, null_frac_net_pf_gt_1=0.5, excess_vs_null=-0.4980. **0 credible candidates.**
  - progress.json: run_id=20261019_135940_grid, n_symbols=275, n_pairs=66, completed_cells=18150, next_cell=null, stopped=false, stop_reason=null, all_symbols_processed=true. 0 blocked.
- Session prep verified: `git status` clean, `git diff --stat` empty, working tree clean on main.

## Next action at/after bound
At/after 2026-10-29T21:24:11.948264+00:00:
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, stop (no provider); re-set wakeup per interval policy.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor from the fresh snapshot; inspect band strictly below floor.
4. If count==0: record pass, set next bound, re-set wakeup, stop.
5. If count>0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol.
6. Update both handoffs with evidence (snapshot_id, counts, results paths) and preserve negative/blocked results.

## Constraints
- No provider before bound; historical research only.
- One 20-page pass max per cycle.
- Do not trigger/cancel/rerun/dispatch GitHub Actions.
- Do not fetch new candle data; do not modify baseline grid or costs/fills/entry-exit.
- Preserve all negative/blocked results.
