# EMA Hourly Continuation — ROSE/USDT P55_144

**Symbol:** ROSE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6707 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -2.7546 |
| sortino_ratio | -0.8707 |
| max_drawdown | 0.6537 |
| cagr | -0.3373 |
| net_avg_win | 53.9839 |
| net_avg_loss | -76.7037 |
| avg_hold_time_bars | 11.3474 |
| exposure | 0.2569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
