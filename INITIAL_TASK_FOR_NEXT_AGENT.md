# Initial Task For Next Agent

Read this handoff first: `NEXT_AGENT_TASK.md`.

## Situation at wakeup (2026-10-29T21:25:00Z)
- Gate bound 2026-10-29T21:24:11.948264+00:00 should have elapsed by now; verify offline before any provider contact.
- Last pass: mcap_snapshot_20261028_212411 (20 pages, 2000 entries). eligible_unseen_below_floor_count==0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES, batch_selected=[].

## Exact steps
1. Check gate offline (`scripts/refresh_gate.py plan` or the `scripts/refresh_gate.py` logic at the current time). If not eligible, re-set wakeup and STOP. Do NOT contact the provider before the bound.
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
- `cancel_wakeup list` returned no pending wakeups for this session.
- Single resume wakeup scheduled: **`wku_184e25a0e0014CZZaZhyQWzHjJ`**, due 2026-10-29T21:25:00Z.
- Do **not** re-schedule a duplicate.