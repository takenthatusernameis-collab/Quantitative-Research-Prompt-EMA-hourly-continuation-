# Initial Task For Next Agent

Read this handoff first: `NEXT_AGENT_TASK.md`.

## Situation at wakeup (2026-10-29T01:12Z)
- Gate bound 2026-10-29T21:24:11.948264+00:00 has NOT elapsed yet. Verified offline this turn
  (2026-10-29T01:12:15.115975+00:00): `gate_status` returns eligible=False (~20h12m remaining).
  Task complete — nothing actionable before the bound. Do NOT contact the provider before the bound.
- Last pass: mcap_snapshot_20261028_212411 (20 pages, 2000 entries, 0 history-probe
  failures). eligible_unseen_below_floor_count==0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES, batch_selected=[].
- A single resume wakeup is scheduled: **wku_18537a5210016Rc5AsWtWz414P**, due
  2026-10-29T21:21:48Z. Do **not** re-schedule a duplicate.
- Baseline grid `results/20261019_135940_grid` re-verified directly: complete
  (all_symbols_processed=true, next_cell=null, stopped=false, stop_reason=null,
  completed_cells=18150 = 275 x 66), 0 blocked, 0 credible candidates, mean net PF
  0.4987.

## Exact steps
1. Check gate offline (`PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`).
   If not eligible, do NOT contact the provider before the bound. The wakeup is already
   scheduled — do not re-schedule a duplicate. STOP.
2. If eligible, run one 20-page pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor; check eligible count below the floor.
4. If 0: record pass, set next bound, re-set wakeup, STOP.
5. If >0: expand per PROMPT.md §2.1 and run full 66-pair grid on each new symbol.

## Hard constraints
- No provider before bound.
- One pass max per cycle.
- No GitHub Actions changes.
- No new candle data; no baseline/cost changes.
- Preserve negative/blocked results.

## Wakeup state (verified this turn)
- Single resume wakeup scheduled: **wku_18537a5210016Rc5AsWtWz414P**, due
  2026-10-29T21:21:48Z (just before the bound at 21:24:11Z).
- Do **not** re-schedule a duplicate.

(End of file - total 38 lines)