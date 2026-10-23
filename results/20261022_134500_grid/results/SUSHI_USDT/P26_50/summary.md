# EMA Hourly Continuation — SUSHI/USDT P26_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.4851 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8867 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -7.9114 |
| sortino_ratio | -3.4554 |
| max_drawdown | 0.9870 |
| cagr | -0.8196 |
| net_avg_win | 22.1362 |
| net_avg_loss | -34.9714 |
| avg_hold_time_bars | 3.8419 |
| exposure | 0.1683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
