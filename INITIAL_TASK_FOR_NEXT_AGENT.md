# INITIAL TASK FOR NEXT AGENT

**Prior agent task completed (2026-10-21T07:33Z).** State reconciled and verified; tests **111 passed**. Grid self-consistent (266×66=17556, all complete, next_cell=null). Universe snapshot band exhausted (0 eligible below TAIKO/USDT $15 436 339); refresh bound still closed until 2026-10-21T11:30:04Z. No CoinGecko query, no code/data changes.

**Read `NEXT_AGENT_TASK.md` first** for verified state, band audit, exact commands, and the new robustness leg.

**Do now (before 2026-10-21T11:30:04Z):** No CoinGecko/data-layer changes — the refresh bound is still closed. Snapshot band exhausted. Offline verification/robustness only over the existing grid. Re-run `python -m pytest tests/ -q` after any changes and report exact results.

**Active work this session (background, must be monitored):** the randomized-entry null leg `scripts/null_grid_scan.py` was checkpointed incomplete — only the `timing` null ran over the whole grid (17 226 of 17 556 cells); the `block` and `sign` nulls ran on only 330 cells. This session started the completion run:

```
PYTHONPATH=. python3 scripts/null_grid_scan.py \
  --run results/20261019_135940_grid \
  --modes block sign --workers 4 --validate-sample 0 \
  --out results/20261021_073300_null_grid_scan
```

It writes `results/20261021_073300_null_grid_scan/cells.jsonl` (append-only, resumable). **Monitor it to completion**, then summarize the grid-wide block/sign null into the handoff (see `NEXT_AGENT_TASK.md` §"New robustness leg"). Do not start a second concurrent run of the same artifact — the checkpoint is resumable.

**From 2026-10-21T11:30:04Z:** Fetch fresh descending ranking (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10`, dry run first; extend pages if coverage stops above floor). Apply eligible names strictly below TAIKO floor in descending mcap order. For each new name: fetch/validate hourly OHLCV (`scripts/fetch_kucoin.py`), run 66-pair EMA grid resuming from `results/20261019_135940_grid` (pass full `--n`, verify `n_symbols x n_pairs == completed_cells`), re-run `scripts/aggregate_grid.py`, `scripts/candidate_check.py`, `scripts/robustness_pooled.py` **and `scripts/oos_grid_scan.py`** (the grid-wide out-of-sample audit must be re-run after every expansion, not just once), update `universe/mcap_expansion_log.md`, `universe/last_scan.json`, `NEXT_AGENT_TASK.md`, and this file.

**Tooling trap:** the grid's artifact layout is not uniform — 330 cells (BTC, ETH, SOL, BNB, XRP, ranks 1-5) still use the legacy uncompressed `trades.csv`, the rest use `trades.csv.gz`. A tool that assumes gzip silently skips the top of the universe. `scripts/oos_grid_scan.py:read_trades` handles both.

Guardrails: append-only, market-cap descending, never stop on negative results, never promote without OOS + 2x-cost + subperiod gates. Run `python -m pytest tests/ -q` and report exact results.