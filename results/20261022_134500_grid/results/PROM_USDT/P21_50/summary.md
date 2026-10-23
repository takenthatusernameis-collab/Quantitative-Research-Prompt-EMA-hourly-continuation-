# EMA Hourly Continuation — PROM/USDT P21_50

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.4103 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.7913 |
| gross_win_rate | 0.4272 |
| sharpe_ratio | -9.7480 |
| sortino_ratio | -4.4152 |
| max_drawdown | 0.9962 |
| cagr | -0.8915 |
| net_avg_win | 17.0717 |
| net_avg_loss | -27.0726 |
| avg_hold_time_bars | 4.6913 |
| exposure | 0.2196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
