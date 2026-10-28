# Initial Task For Next Agent

Read this handoff first: `NEXT_AGENT_TASK.md` (durable state + exact next action).

## Situation at wakeup (due ~2026-10-28T19:35Z)

Gate is NOT eligible: bound `2026-10-28T19:29:54.929656+00:00` has not yet elapsed (last pass `mcap_snapshot_20261027_192954`, CoinGecko 20/20 pages, 2000 entries). Wakeup id: `wku_17ff7c285001GFseGBR5ciimvT` (due ~2026-10-28T19:45:06Z). Re-checked offline at 2026-10-28T00:43Z — gate remains `eligible=False`. No provider contact is permitted before the bound elapses.

## Your next action (run this turn)

1. Check the gate offline:
   `PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`
   - If still `eligible=False`: re-set a wakeup at/after the bound (e.g. at 2026-10-28T19:35:00Z or later) and STOP — no provider contact, nothing else to do. Update both handoffs with the re-set wakeup id.
   - If `eligible=True`: proceed to step 2.

2. Run exactly one 20-page CoinGecko ranking pass:
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`
   (One pass max per cycle; never poll CoinGecko while waiting.)

3. Recompute the expansion floor from the fresh snapshot; inspect the band strictly below the floor (floor was ALPINE/USDT $3 489 697 at the last scan).

4. If `eligible_unseen_below_floor_count == 0`: record the pass in `universe/last_scan.json` (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `batch_selected = []`) and set a +24 h bound (`next_eligible_refresh_at = scanned_at + 24 h`). Then re-set a wakeup at/after that bound and STOP.

5. Else (eligible names exist): expand per PROMPT.md §2.1 (append next lower market-cap names, update `universe/mcap_rank.json` + `universe/mcap_expansion_log.md`, then run the full 66-pair grid on each new symbol).

6. Update both handoffs (`NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`) with the result: gate check outcome, snapshot id/pages, floor, eligible count, batch, next bound/wakeup id.

## Constraints (hard)

- No provider before bound; historical research only; never describe fixtures as market evidence.
- Do not trigger, cancel, rerun, or dispatch GitHub Actions; do not edit workflow files.
- Do not fetch new candle data; do not modify the baseline grid or registered costs/fills/entry-exit semantics.
- Preserve all negative and blocked results; never label a partial grid complete.
- A negative result is a valid research result; expand rather than stop.

## Static context (unchanged this turn)

- Universe N = 275; expansion floor ALPINE/USDT $3 489 697; `eligible_unseen_below_floor_count = 0`; `batch_selected = []`; no universe expansion this turn.
- Baseline grid results/20261019_135940_grid: all symbols processed, 18150 cells, pooled mean net PF 0.4987, **0 credible candidates**.
- Child mutation grids C_min_risk_atr and C_stricter_trend: complete, NOT_PROMOTED; baseline grid remains the program grid (results/mutations.json).
- `git status --short` empty; `pytest tests/ -q` -> 248 passed, 1 failed (pre-existing clock bug test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible, left untouched per AGENTS.md #6).
