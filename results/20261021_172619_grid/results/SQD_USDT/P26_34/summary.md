# EMA Hourly Continuation — SQD/USDT P26_34

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.8561 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0896 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.7004 |
| sortino_ratio | -0.1509 |
| max_drawdown | 0.1831 |
| cagr | -0.0683 |
| net_avg_win | 83.1339 |
| net_avg_loss | -106.5339 |
| avg_hold_time_bars | 5.9213 |
| exposure | 0.0601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
