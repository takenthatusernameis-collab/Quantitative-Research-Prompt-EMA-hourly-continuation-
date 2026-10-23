# EMA Hourly Continuation — POLYX/USDT P21_100

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6559 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9516 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -3.3813 |
| sortino_ratio | -1.1734 |
| max_drawdown | 0.7682 |
| cagr | -0.4267 |
| net_avg_win | 49.1314 |
| net_avg_loss | -69.8831 |
| avg_hold_time_bars | 15.3967 |
| exposure | 0.4234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
