# INITIAL TASK FOR NEXT AGENT

## Current state (turn 2026-10-29T13:20:25Z)

- Gate re-verified offline: `{'eligible': False, 'bound': '2026-10-29T21:24:11.948264+00:00', 'now': '2026-10-29T13:20:25.162630+00:00', 'reason': 'the 24 h refresh bound 2026-10-29T21:24:11.948264+00:00 has not elapsed yet'}` — ~8 h remaining. Nothing actionable until the bound elapses.
- Working tree clean (`git status --short` empty). No provider contact; no changes made.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`; snapshot `mcap_snapshot_20261028_212411`; universe N=275; expansion floor `ALPINE/USDT` $3,472,967; `eligible_unseen_below_floor_count: 0`; `batch_selected: []`; `next_eligible_refresh_at: 2026-10-29T21:24:11.948264+00:00`.
- Coverage 20/20 pages, 2000 entries, lowest mcap $3,410,633 (below floor), `coverage_reaches_below_floor: true`.
- Single resume wakeup already set for **2026-10-29T21:27:15Z** (cross-session; not visible in this session's `cancel_wakeup list`). **Do NOT create a second wakeup; let it fire.**

## Task (at/after 2026-10-29T21:24:11.948264+00:00)

1. Check the gate offline first:
   `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`
   - If not eligible: stop (no provider), re-set wakeup per 24 h policy, update both handoffs.
   - If eligible: run exactly one 20-page pass
     `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`
     recompute expansion floor from fresh snapshot; inspect band strictly below floor.
2. If `eligible_unseen_below_floor_count == 0`: record the pass, set `next_eligible_refresh_at`, re-set wakeup, stop (no expand).
3. If count > 0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol via `scripts/run_grid.py` (or tested resume path), re-aggregate.
4. Update both handoffs with evidence (snapshot_id, counts, results paths); preserve all negative/blocked results.

## Constraints

- No provider before the bound; one 20-page pass max per cycle; do not fetch new candle data; do not modify baseline grid/costs/fills/entry-exit semantics; do not create a second wakeup (resume wakeup already set for 2026-10-29T21:27:15Z).
