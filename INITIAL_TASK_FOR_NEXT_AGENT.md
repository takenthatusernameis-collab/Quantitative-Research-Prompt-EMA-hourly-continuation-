# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z (re-verified 2026-10-24T09:08:13 UTC, gate eligible=False, bound not elapsed)
## Initial task message for the next agent

The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES` after batch 28 (2026-10-23T12:28:28Z pass found 0 eligible unseen names below the floor; 2000-entry CoinGecko ranking band exhausted down to $3,441,774). Universe n=275. The 24h refresh bound expires at 2026-10-24T12:28:28.949476Z. **Do not** contact CoinGecko/KuCoin before that timestamp.

This session (2026-10-24T09:08:13Z) re-verified the gate offline: `eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now `2026-10-24T09:08:13.560503+00:00`. Reason: bound not elapsed (~3h 20m remaining). No provider contact made. Tests run: 25 passed, 1 pre-known clock-relative failure (`test_the_classic_path_records_the_bound_even_when_names_are_eligible` — do not loosen the gate). Scheduled wakeup `wku_16d2c4e39001y16qan5hr5dca1` at 2026-10-24T12:29:00Z to run the refresh pass per steps below. State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=275`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`. Baseline grid `results/20261019_135940_grid` complete (18150/18150 cells, 275 symbols x 66 pairs, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, 0 blocked — `completed` list length 18150, no "blocked" substring anywhere in `progress.json`; `summary.json` pooled: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14 676 563, mean_net_pf 0.4987, median 0.5198, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, n_blocked 0, credible candidates 0).

## Steps
1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable.

2. **Run exactly one 20-page market-cap ranking pass:**
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   Only provider contact this cycle. Freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** for `eligible_unseen_below_floor_count`.

4. **If candidates exist:** expand per PROMPT.md §2.1 — append descending market-cap candidates (track previous→new N, rank range, log to `universe/mcap_expansion_log.md` with source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`, then `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`, set `universe/last_scan.json` state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound becomes +24h from new scan time.

6. **Update handoffs:** after completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with new bound and next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No candidates exist; awaiting new eligible names from next 20-page pass at/after bound.

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
