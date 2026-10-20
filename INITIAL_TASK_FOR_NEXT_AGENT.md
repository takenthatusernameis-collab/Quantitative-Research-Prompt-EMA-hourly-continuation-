# INITIAL TASK FOR NEXT AGENT

The EMA hourly-continuation research program has completed **Batch 18 (N = 187; 12 342/12 342 EMA-grid cells)**. The latest OOS + 2x transaction-cost candidate check found **0 credible candidates**. This is a negative research result for the current strategy rules, but it is **not** authorization to stop the market-cap expansion program.

Current status: **`EXPANSION_AVAILABLE`** - the universe is not exhausted.
- Universe N = 187, floor **SSV/USDT at USD 37 149 593**; last ranking snapshot `universe/mcap_snapshot_20261020_113004` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 entries down to $15.17M - the pass reaches below the floor).
- That snapshot still holds **79 eligible unseen names below the floor**, so batch 19 can be applied straight from the saved snapshot. **Do not wait 24 hours and do not re-query CoinGecko** (the 24h bound only applies after a pass that finds zero eligible names). `universe/last_scan.json` records `state=EXPANSION_AVAILABLE`, floor `SSV/USDT 37 149 593`, and the 10 selected names.
- Batch 19 (verified by dry run at 2026-10-20T13:07Z): OSMO, MOODENG, MEW, MERL, RPL, MOCA, UMA, DEGEN, ORBS, CATI.

Read `NEXT_AGENT_TASK.md` first. It contains the exact next steps for applying the batch from the saved snapshot, fetching and validating the 9 missing hourly fixtures, appending the universe in market-cap order, running all 66 EMA pairs per new symbol, re-running the aggregate and robustness checks, and persisting the results. Existing symbols/results are append-only; do not re-run completed grid cells.

Current key metrics: mean net PF 0.4934; median net PF 0.5134; best in-sample PF 2.2274 (BABYDOGE/USDT P50_55) but rejected for zero OOS trades; 35 cells had net PF > 1 and all failed OOS/cost stress; 10,110,532 aggregate trades; 0 credible candidates. All backtest metrics are historical research estimates, not live performance.

Guardrails: no fabricated symbols, no silent baseline/parameter changes, no lowering of data requirements, and no in-sample-only promotion. Run `python -m pytest tests/ -q` after code changes and report the actual result.

- Session note (2026-10-20T13:10:00Z): completed the batch-18 grid (ETN, PEOPLE, IOTX, SSV), re-ran the aggregate and candidate check (0 credible candidates, artifact `results/20261020_125819_candidate_check/`), verified all 660 batch-18 cells, updated `universe/mcap_expansion_log.md`, and confirmed the batch-19 selection from the saved snapshot. Tests verified 56 passed; no code changes.
