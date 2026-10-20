# INITIAL TASK FOR NEXT AGENT

The EMA hourly-continuation research program has completed Batch 17 (N=177; 11,682/11,682 EMA-grid cells). The latest OOS + 2x transaction-cost candidate check found **0 credible candidates**. This is a negative research result for the current strategy rules, but it is **not authorization to stop the market-cap expansion program permanently**.

Current status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`.
- Last recorded ranking snapshot used for expansion: `mcap_snapshot_20261020_082835` (N=177, floor BOME ~USD 41.20M).
- Fresh full ranking scan completed 2026-10-20T10:02:36Z using `mcap_snapshot_20261020_100236.json` (pages 1–5, 500 entries). **No eligible unseen symbols below the current floor found** (GAS/USDT ~80.37M was above floor; symbols below floor in prior snapshot were not present as eligible KuCoin spot USDT pairs in the fresh snapshot). Next eligible refresh **>= 2026-10-21T10:02:36Z** (≥24h after the empty complete scan).

Read `NEXT_AGENT_TASK.md` first. It contains the exact next steps for checking snapshot freshness, validating new assets, appending the universe in market-cap order, fetching data, completing all 66 EMA pairs for each added symbol, re-running robustness checks and persisting results. Existing symbols/results are append-only; do not re-run completed grid cells.

Current key metrics: mean net PF 0.4917; median net PF 0.5112; best in-sample PF 2.2274 but rejected for zero OOS trades; 35 cells had net PF > 1 and all failed OOS/cost stress; 9,567,069 aggregate trades; 0 credible candidates. All backtest metrics are historical research estimates, not live performance.

Guardrails: no fabricated symbols, no silent baseline/parameter changes, no lowering of data requirements, and no in-sample-only promotion. Run `python -m pytest tests/ -q` after code changes and report the actual result.
