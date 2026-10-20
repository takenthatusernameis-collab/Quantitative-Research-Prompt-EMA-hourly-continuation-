# EMA Hourly Continuation — DAG/USDT P26_55

**Symbol:** DAG/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.3420 |
| net_win_rate | 0.3881 |
| gross_profit_factor | 0.5818 |
| gross_win_rate | 0.3987 |
| sharpe_ratio | -9.5510 |
| sortino_ratio | -4.1054 |
| max_drawdown | 0.9952 |
| cagr | -0.8794 |
| net_avg_win | 14.2111 |
| net_avg_loss | -26.3477 |
| avg_hold_time_bars | 3.5107 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
