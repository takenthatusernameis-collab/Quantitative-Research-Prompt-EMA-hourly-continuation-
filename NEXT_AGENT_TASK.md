# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-29T05:33Z)
- Gate checked offline: eligible=False (bound 2026-10-29T21:24:11.948264+00:00 not yet elapsed; ~15h51m remaining). No provider contact made. Verified via `scripts.refresh_gate.gate_status`.
- Wakeup: a single resume wakeup is set just after the bound (~2026-10-29T21:29:00Z). Do NOT create a second one; let it fire.
- Last scan: mcap_snapshot_20261028_212411 (2000 entries, 20/20 pages). eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor recomputed from fresh snapshot at pass time — do not assume values without recomputing.
- next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.

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
