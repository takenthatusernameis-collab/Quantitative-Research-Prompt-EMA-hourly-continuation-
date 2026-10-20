# EMA Hourly Continuation — LQTY/USDT P20_50

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8606 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -6.6574 |
| sortino_ratio | -2.9784 |
| max_drawdown | 0.9742 |
| cagr | -0.7624 |
| net_avg_win | 21.5756 |
| net_avg_loss | -35.9778 |
| avg_hold_time_bars | 5.5258 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
