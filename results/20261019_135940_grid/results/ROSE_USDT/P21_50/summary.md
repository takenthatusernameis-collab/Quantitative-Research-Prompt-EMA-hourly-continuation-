# EMA Hourly Continuation — ROSE/USDT P21_50

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.6106 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 1.0142 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -6.5893 |
| sortino_ratio | -3.0120 |
| max_drawdown | 0.9749 |
| cagr | -0.7636 |
| net_avg_win | 31.7933 |
| net_avg_loss | -44.2363 |
| avg_hold_time_bars | 4.6641 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
