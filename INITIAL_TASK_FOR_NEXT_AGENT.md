# INITIAL TASK FOR NEXT AGENT

At/after 2026-10-29T21:24:11.948264+00:00:

1. Check the gate offline first:
   PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
   - If not eligible: stop (no provider), re-set wakeup per 24 h policy, update both handoffs.
   - If eligible: run exactly one 20-page pass
     PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
     recompute expansion floor from fresh snapshot; inspect band strictly below floor.
2. If eligible_unseen_below_floor_count == 0: record the pass, set next_eligible_refresh_at, re-set wakeup, stop (no expand).
3. If count > 0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol via scripts/run_grid.py (or tested resume path), re-aggregate.
4. Update both handoffs with evidence (snapshot_id, counts, results paths); preserve all negative/blocked results.

Constraints: no provider before the bound; one 20-page pass max per cycle; do not fetch new candle data; do not modify baseline grid/costs/fills/entry-exit semantics; do not create a second wakeup (resume wakeup already set for 2026-10-29T21:27:15Z).
