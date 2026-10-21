# EMA Hourly Continuation — RAY/USDT P8_12

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.7274 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0177 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.6497 |
| sortino_ratio | -0.4005 |
| max_drawdown | 0.4109 |
| cagr | -0.1685 |
| net_avg_win | 68.2276 |
| net_avg_loss | -96.4620 |
| avg_hold_time_bars | 4.2867 |
| exposure | 0.0557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
