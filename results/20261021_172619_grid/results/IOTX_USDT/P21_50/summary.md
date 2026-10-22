# EMA Hourly Continuation — IOTX/USDT P21_50

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7415 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0318 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -2.1668 |
| sortino_ratio | -0.7103 |
| max_drawdown | 0.5919 |
| cagr | -0.2773 |
| net_avg_win | 60.3447 |
| net_avg_loss | -84.9111 |
| avg_hold_time_bars | 6.5453 |
| exposure | 0.1544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
