# INITIAL TASK FOR NEXT AGENT

State at handoff (2026-10-29T14:27:45Z): gate closed, ~6h 56m to bound. Working tree clean. Snapshot mcap_snapshot_20261028_212411, universe N=275, floor ALPINE/USDT $3,472,967, eligible_unseen_below_floor_count 0, state AWAITING_NEW_ELIGIBLE_CANDIDATES. Wakeup re-set for 2026-10-29T21:27:15Z (id wku_1880fd2d2001lAT14fqLpI31gM; do NOT create a second). Baseline grid complete (18150 cells, 0 credible), child mutation C_min_risk_atr complete but not promoted.

Do this at/after 2026-10-29T21:24:11.948264+00:00:

1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible: stop (no provider), re-set wakeup per 24h policy, update NEXT_AGENT_TASK.md and this file with evidence.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`. Recompute expansion floor from fresh snapshot; inspect band strictly below floor for `eligible_unseen_below_floor_count`.
3. If count==0: record pass, set `next_eligible_refresh_at` (per policy), re-set wakeup, stop (no expansion). Update handoffs with snapshot_id/counts/paths.
4. If count>0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol via `scripts/run_grid.py` (or tested resume path), re-aggregate. Update handoffs with evidence (snapshot_id, counts, results paths). Preserve all negative/blocked results.
5. Constraints: historical research only; no orders/live/paper trading; no provider before bound; 1 pass max/cycle; do not fetch new candle data; do not modify baseline grid/costs/fills/entry-exit semantics; do not trigger/cancel/rerun GitHub Actions or edit workflows; do not create second wakeup; keep strict confirmatory separate from exploratory.

Update both files with exact evidence and one measurable next task.