# EMA Hourly Continuation — BIGTIME/USDT P100_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.7619 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -1.3975 |
| sortino_ratio | -0.3356 |
| max_drawdown | 0.3390 |
| cagr | -0.1429 |
| net_avg_win | 73.6742 |
| net_avg_loss | -94.0088 |
| avg_hold_time_bars | 12.5951 |
| exposure | 0.1619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
