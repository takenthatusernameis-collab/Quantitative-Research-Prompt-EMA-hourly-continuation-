# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-29T04:16:22Z)
- Gate rechecked offline now: eligible=False (bound 2026-10-29T21:24:11.948264+00:00 not yet elapsed; ~17h 8m remaining). No provider contact made. `git status --short` and `git diff --stat` empty.
- Wakeup already set: **wku_185af5e44001at3cF6d2tO4E7R** due 2026-10-29T21:26:21Z. Do NOT create a second one; let it fire.
- Last scan: mcap_snapshot_20261028_212411 (2000 entries, 20/20 pages). eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor ALPINE/USDT $3,472,967 (last_scan.json) / $3,614,141 (mcap_rank.json). Floor used by gate is recomputed by `fetch_mcap_snapshot.py` from the fresh snapshot at pass time — do not assume values without recomputing.
- next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Baseline grid results/20261019_135940_grid verified: n_cells 18150, n_symbols 275, n_pairs 66, mean net PF 0.4987; complete, 0 blocked, 0 credible candidates.

## Next action at/after bound
At/after 2026-10-29T21:24:11.948264+00:00:
1. Check gate offline: `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`. If not eligible, re-set wakeup (keep interval policy) and stop.
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
