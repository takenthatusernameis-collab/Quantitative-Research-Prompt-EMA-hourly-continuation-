# INITIAL TASK FOR NEXT AGENT

The EMA hourly-continuation research program has completed Batch 17 (N=177; 11,682/11,682 EMA-grid cells). The latest OOS + 2x transaction-cost candidate check found **0 credible candidates**. This is a negative research result for the current strategy rules, but it is **not authorization to stop the market-cap expansion program permanently**.

Current status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`. The last recorded ranking snapshot is `mcap_snapshot_20261020_082835`; the existing handoff reports that the checked ranking pages 4–5 yielded no currently eligible new symbols below the BOME market-cap floor. Do not invent an immediate batch 18, and do not repeatedly query the provider every five minutes. Re-check the complete descending ranking at a bounded cadence (at most once per 24 hours after an empty complete scan) and append the next batch when genuinely new eligible candidates appear.

Read `NEXT_AGENT_TASK.md` first. It contains the exact next steps for checking snapshot freshness, validating new assets, appending the universe in market-cap order, fetching data, completing all 66 EMA pairs for each added symbol, re-running robustness checks and persisting results. Existing symbols/results are append-only; do not re-run completed grid cells.

Current key metrics: mean net PF 0.4917; median net PF 0.5112; best in-sample PF 2.2274 but rejected for zero OOS trades; 35 cells had net PF > 1 and all failed OOS/cost stress; 9,567,069 aggregate trades; 0 credible candidates. All backtest metrics are historical research estimates, not live performance.

Guardrails: no fabricated symbols, no silent baseline/parameter changes, no lowering of data requirements, and no in-sample-only promotion. Run `python -m pytest tests/ -q` after code changes and report the actual result.
