# INITIAL TASK FOR NEXT AGENT

**Prior agent task completed (2026-10-21T00:12:45Z).** Batch 26 done (N=266, 17556/17556 cells, 0 credible candidates). State: **AWAITING_NEW_ELIGIBLE_CANDIDATES**, re-verified; tests **67 passed**. Grid state self-consistent (266×66=17556, all complete, next_cell=null). Universe snapshot band exhausted (0 eligible below TAIKO/USDT $15,436,339); refresh bound opens at 2026-10-21T11:30:04Z.

**Read `NEXT_AGENT_TASK.md` first** for verified state, band audit, robustness results, grid fix, and exact commands.

**Do now (before 2026-10-21T11:30:04Z):** No CoinGecko/data-layer changes. Snapshot band exhausted. Offline verification/robustness only over existing grid. `python -m pytest tests/ -q` -> 67 passed (re-run after any change).

**From 2026-10-21T11:30:04Z:** Fetch fresh descending ranking (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10`, dry run first; extend pages if coverage stops above floor), apply eligible names strictly below TAIKO floor in descending mcap order. For each new name: fetch/validate hourly OHLCV (`scripts/fetch_kucoin.py`), run 66-pair EMA grid resuming from `results/20261019_135940_grid` (pass full `--n`, verify `n_symbols x n_pairs == completed_cells`), re-run `scripts/aggregate_grid.py`, `scripts/candidate_check.py`, `scripts/robustness_pooled.py`, update `universe/mcap_expansion_log.md`, `universe/last_scan.json`, `NEXT_AGENT_TASK.md`, and this file.

Guardrails: append-only, market-cap descending, never stop on negative results, never promote without OOS + 2x-cost + subperiod gates. Run `python -m pytest tests/ -q` and report exact result.