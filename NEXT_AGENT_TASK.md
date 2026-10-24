# NEXT AGENT TASK — Durable Handoff (verified 2026-10-24T21:29:08Z; gate eligible=False, bound NOT yet elapsed)
## Current state
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- Offline gate re-verified 2026-10-24T21:29:01.625878+00:00: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (~17h 1m remaining); no provider contact made. Wakeup `wku_16fcd6dc2001hddUtJFTA4Q12X` at 2026-10-25T14:31:00Z to resume at the bound.
- Baseline grid re-verified via `results/20261019_135940_grid/progress.json`: 275 symbols × 66 pairs, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, 0 blocked. `summary.json` pooled: mean net PF 0.4987, median 0.5198, best net PF 2.2274, n_cells_net_pf_gt_1 37, n_rejected 18123, n_blocked 0, **0 credible candidates**.
- Universe: **N = 275** symbols (BTC/USDT ... ALPINE/USDT), ranked strictly market-cap descending, append-only.
- Last scan (Batch 29): `universe/mcap_snapshot_20261024_143039.json` (2026-10-24T14:30:39.449637Z, 20/20 pages, 2000 entries, lowest covered $3,363,414). Floor `CWEB/USDT` $3,888,825. `eligible_unseen_below_floor_count = 0`. State set back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Next bound `2026-10-25T14:30:39.449637+00:00`.

## Your task (run at/after 2026-10-25T14:30:39.449637+00:00)
**Do NOT** contact CoinGecko/KuCoin before that timestamp.

1. Verify eligibility offline:
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report the bound — nothing is actionable.

2. Run exactly one 20-page ranking pass (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```

3. Re-check `eligible_unseen_below_floor_count` against the new floor.

4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N → new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run the full 66-pair EMA grid per new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`, then `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.

6. Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and the next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. Awaiting new eligible names from the next 20-page pass at/after the bound 2026-10-25T14:30:39.449637+00:00.

## Constraints
- No provider call before 2026-10-25T14:30:39.449637+00:00.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
- Do not stop the program on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen the gate.
- Wakeup `wku_16fcd6dc2001hddUtJFTA4Q12X` at 2026-10-25T14:31:00Z to resume this task at the bound; do not re-schedule a duplicate.
