# Initial Task For Next Agent

Read this handoff first: `NEXT_AGENT_TASK.md`.

## Situation at wakeup (2026-10-28T23:46Z)
- Gate bound 2026-10-29T21:24:11.948264+00:00 has NOT elapsed yet. Verified offline:
  `gate_status` returns eligible=False. Do NOT contact the provider before the bound.
- Last pass: mcap_snapshot_20261028_212411 (20 pages, 2000 entries, 0 history-probe
  failures). eligible_unseen_below_floor_count==0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES, batch_selected=[].
- A single resume wakeup is scheduled: **wku_184eae640001zsEIDct3nJ5dh2**, due
  2026-10-29T21:25:00Z. The previous wakeup was already gone on arrival; do not
  re-schedule a duplicate.

## Exact steps
1. Check gate offline (`PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`).
   If not eligible, re-set wakeup and STOP. Do NOT contact the provider before the bound.
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
- `cancel_wakeup list` returned no pending wakeups for this session at 2026-10-28T23:48Z.
- Single resume wakeup scheduled: **wku_184eae640001zsEIDct3nJ5dh2**, due 2026-10-29T21:25:00Z.
- Do **not** re-schedule a duplicate.