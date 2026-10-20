# EMA Hourly Continuation — MERL/USDT P21_55

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 897 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8199 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -5.4910 |
| sortino_ratio | -2.3101 |
| max_drawdown | 0.9423 |
| cagr | -0.6712 |
| net_avg_win | 29.0708 |
| net_avg_loss | -42.8550 |
| avg_hold_time_bars | 6.2765 |
| exposure | 0.2566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
