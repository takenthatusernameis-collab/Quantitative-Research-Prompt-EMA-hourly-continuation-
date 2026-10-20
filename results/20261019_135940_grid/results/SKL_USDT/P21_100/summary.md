# EMA Hourly Continuation — SKL/USDT P21_100

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 1.0084 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -3.0008 |
| sortino_ratio | -1.0791 |
| max_drawdown | 0.7489 |
| cagr | -0.3957 |
| net_avg_win | 49.5751 |
| net_avg_loss | -70.8104 |
| avg_hold_time_bars | 14.9688 |
| exposure | 0.4368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
