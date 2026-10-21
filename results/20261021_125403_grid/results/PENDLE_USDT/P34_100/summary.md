# EMA Hourly Continuation — PENDLE/USDT P34_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.2861 |
| sortino_ratio | -0.3817 |
| max_drawdown | 0.4056 |
| cagr | -0.1625 |
| net_avg_win | 71.5063 |
| net_avg_loss | -88.6344 |
| avg_hold_time_bars | 13.2937 |
| exposure | 0.2592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
