# Initial Task For Next Agent

Read this handoff first: `NEXT_AGENT_TASK.md`.

## Situation at wakeup
- Gate ELIGIBLE at/after `2026-10-29T21:24:11.948264+00:00`. Currently NOT eligible (bound in future).
- Last pass: `mcap_snapshot_20261028_212411` (20 pages, 2000 entries). `eligible_unseen_below_floor_count==0`.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, batch_selected=[].
- Wakeup `wku_184733715001WiGivAnbwERwwu` due 2026-10-29T21:38:25.681Z.

## Exact steps
1. Check gate offline. If not eligible, re-set wakeup and STOP.
2. If eligible, run one 20-page pass.
3. Recompute floor; check eligible count.
4. If 0: record, set next bound, re-set wakeup, STOP.
5. If >0: expand and run grid.

## Hard constraints
- No provider before bound.
- One pass max per cycle.
- No GitHub Actions changes.
- No new candle data; no baseline/cost changes.
- Preserve negative/blocked results.
