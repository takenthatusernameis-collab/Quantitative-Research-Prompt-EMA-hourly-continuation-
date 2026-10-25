# INITIAL TASK MESSAGE FOR NEXT AGENT (re-verified 2026-10-25T07:48:40Z)
## Context
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES` (Batch 29 done 2026-10-24T14:30:39Z). Found 0 eligible unseen names below floor; 2000-entry CoinGecko band exhausted down to ~3363414. Universe N=275 (BTC/USDT ... CWEB/USDT).
- Offline gate re-verified **2026-10-25T07:48:40Z**: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed. No provider contact made.
- Baseline grid `results/20261019_135940_grid` re-verified via `progress.json`: `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150` (275x66), 0 blocked. `summary.json` pooled: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14676563, mean net PF 0.4987, median 0.5198, best net PF 2.2274, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, **0 credible candidates**.
- Wakeup `wku_17208a9d9001tjGMBg3arOtd6b` at `2026-10-25T14:31:00Z` to resume at the bound. Do not re-schedule a duplicate.
- Session prep (verified this turn): `git status --short` empty, `git diff --stat` empty.

## Required action (at/after bound)
**Do NOT** contact CoinGecko/KuCoin before 2026-10-25T14:30:39.449637+00:00.

1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable.

2. **Run exactly one 20-page market-cap ranking pass** (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   Freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** for `eligible_unseen_below_floor_count`.

4. **If candidates exist:** expand per PROMPT.md §2.1 — append descending market-cap candidates, log to `universe/mcap_expansion_log.md` with source/date, fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with:
   ```bash
   PYTHONPATH=. python3 scripts/run_grid.py --mcap universe/mcap_rank.json --n <NEW_TOTAL_N> --fixture-base data/fixtures --resume results/20261019_135940_grid
   ```
   Then `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** record pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound becomes +24h from new scan time.

6. **Update handoffs:** update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with new bound and next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No candidates exist currently; awaiting new eligible names from next 20-page pass at/after bound 2026-10-25T14:30:39.449637+00:00.

## Constraints
- No provider contact before 2026-10-25T14:30:39.449637+00:00
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
- Wakeup `wku_17208a9d9001tjGMBg3arOtd6b` at `2026-10-25T14:31:00Z` to resume this task at the bound; do not re-schedule a duplicate.