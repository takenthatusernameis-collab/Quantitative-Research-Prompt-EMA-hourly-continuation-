# INITIAL TASK FOR NEXT AGENT

**Prior agent task completed (2026-10-21T04:49Z).** Batch 26 done (N=266, 17556/17556 cells, 0 credible candidates). State: **AWAITING_NEW_ELIGIBLE_CANDIDATES**, re-verified; tests **110 passed**. Grid state self-consistent (266×66=17556, all complete, next_cell=null). Universe snapshot band exhausted (0 eligible below TAIKO/USDT $15,436,339); refresh bound opens at 2026-10-21T11:30:04Z. The wait was spent on offline verification, not idling.

**Read `NEXT_AGENT_TASK.md` first** for verified state, band audit, exact commands, and the new robustness leg.

**Do now (before 2026-10-21T11:30:04Z):** No CoinGecko/data-layer changes — the refresh bound is still closed. Snapshot band exhausted. Offline verification/robustness only over the existing grid. Re-run `python -m pytest tests/ -q` after any changes.

**From 2026-10-21T11:30:04Z:** Fetch fresh descending ranking (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10`, dry run first; extend pages if coverage stops above floor). Apply eligible names strictly below TAIKO floor in descending mcap order. For each new name: fetch/validate hourly OHLCV (`scripts/fetch_kucoin.py`), run 66-pair EMA grid resuming from `results/20261019_135940_grid` (pass full `--n`, verify `n_symbols x n_pairs == completed_cells`), re-run `scripts/aggregate_grid.py`, `scripts/candidate_check.py`, `scripts/robustness_pooled.py` **and `scripts/oos_grid_scan.py`** (the grid-wide out-of-sample audit must be re-run after every expansion, not just once), update `universe/mcap_expansion_log.md`, `universe/last_scan.json`, `NEXT_AGENT_TASK.md`, and this file.

**Tooling trap:** the grid's artifact layout is not uniform — 330 cells (BTC, ETH, SOL, BNB, XRP, ranks 1-5) still use the legacy uncompressed `trades.csv`, the rest use `trades.csv.gz`. A tool that assumes gzip silently skips the top of the universe. `scripts/oos_grid_scan.py:read_trades` handles both.

Guardrails: append-only, market-cap descending, never stop on negative results, never promote without OOS + 2x-cost + subperiod gates. Run `python -m pytest tests/ -q` and report exact result.
"
filePath">
/home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-/INITIAL_TASK_FOR_NEXT_AGENT.md