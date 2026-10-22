# EMA Hourly Continuation — PENDLE/USDT P26_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.5787 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.7858 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -3.2376 |
| sortino_ratio | -0.8344 |
| max_drawdown | 0.6664 |
| cagr | -0.3361 |
| net_avg_win | 58.4396 |
| net_avg_loss | -78.2035 |
| avg_hold_time_bars | 41.2283 |
| exposure | 0.6484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
