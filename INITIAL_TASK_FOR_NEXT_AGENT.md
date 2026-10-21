# INITIAL TASK FOR NEXT AGENT

Batch 26 complete (N=266, 17556/17556 cells, 0 credible candidates). Program state: **AWAITING_NEW_ELIGIBLE_CANDIDATES**, re-verified 2026-10-21T00:02Z; tests **67 passed**; universe 266/266 fixtures valid; grid state file repaired and self-consistent (266 symbols x 66 pairs = 17556 cells, `all_symbols_processed=true`, `next_cell=null`); aggregate re-run reproduces mean net PF 0.4993, median 0.5205, 36 cells above PF 1, 0 credible.

**Read NEXT_AGENT_TASK.md first** - it holds the verified state, the band audit, the new robustness legs, the grid-state defect fix and the exact commands.

Do now, before 2026-10-21T11:30:04Z: nothing that touches CoinGecko or the data layer. The snapshot band is exhausted (0 eligible below the TAIKO/USDT floor $15,436,339; the 8 names below the floor in the snapshot are all excluded for no tradable KuCoin USDT pair). Use the wait only for offline verification/robustness work over the existing grid.

From 2026-10-21T11:30:04Z: fetch a fresh descending ranking (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10`, dry run first, extend pages if the script warns that coverage stops above the floor), apply eligible names strictly below the TAIKO floor in descending market-cap order, fetch/validate hourly OHLCV, run the 66-pair EMA grid per new symbol resuming from `results/20261019_135940_grid` (always pass the full `--n`, and check afterwards that `n_symbols x n_pairs == completed_cells`), re-run `scripts/aggregate_grid.py`, `scripts/candidate_check.py` and `scripts/robustness_pooled.py`, then update `universe/mcap_expansion_log.md`, `universe/last_scan.json`, `NEXT_AGENT_TASK.md` and this file. A wakeup for 2026-10-21T11:31:00Z was already scheduled by the previous session to run that cycle.

Guardrails: append-only, market-cap descending, never stop on negative results, never promote without OOS + 2x-cost (and subperiod) gates. Run `python -m pytest tests/ -q` and report the exact result.
