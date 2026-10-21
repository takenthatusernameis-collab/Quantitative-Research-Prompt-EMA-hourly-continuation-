# EMA Hourly Continuation — PENDLE/USDT P50_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8073 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.2449 |
| sortino_ratio | -0.3488 |
| max_drawdown | 0.4122 |
| cagr | -0.1494 |
| net_avg_win | 72.4963 |
| net_avg_loss | -92.1844 |
| avg_hold_time_bars | 7.6457 |
| exposure | 0.1324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
