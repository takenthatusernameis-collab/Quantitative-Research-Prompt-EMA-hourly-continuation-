# Initial Task Message for Next Agent

## When the wakeup fires (at/after 2026-10-29T21:30:00Z, just after the bound)

Re-run the offline gate check:

```bash
PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
```

## Decision tree

- **Not eligible** -> stop. Do **not** call the provider. Re-set a single wakeup just after the bound `2026-10-29T21:24:11.948264+00:00` and wait again.
- **Eligible** -> run exactly one 20-page pass:
  ```bash
  PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
  ```
  Recompute the expansion floor and inspect `eligible_unseen_below_floor_count`:
  - If `0`: record the pass, set `next_eligible_refresh_at`, re-set a single wakeup just after the new bound, stop.
  - If `>0`: expand per PROMPT.md §2.1, run the full 66-pair grid per new symbol via `scripts/run_grid.py`, then re-aggregate.

## Constraints (unchanged)

Historical research only; no orders/live/paper trading; **no provider before the bound**; 1 pass max/cycle; do not fetch new candle data; do not modify baseline grid/costs/fills/entry-exit semantics; do not trigger/cancel/rerun GitHub Actions or edit workflows; **single wakeup only**; keep confirmatory separate from exploratory.

## Evidence (this cycle, 2026-10-29T17:18:01Z)

- Gate status: NOT ELIGIBLE, bound `2026-10-29T21:24:11.948264+00:00`.
- Wakeup `wku_188ab5b2c001TGfD2kIH5ZqvXp` scheduled for `2026-10-29T21:30:00Z`.
- Universe: snapshot `mcap_snapshot_20261028_212411`, N=275, floor ALPINE/USDT $3,472,967, `eligible_unseen_below_floor_count` = 0, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`.
- Git status: clean.