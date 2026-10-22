# EMA Hourly Continuation — KAS/USDT P21_55

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.4306 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8329 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -6.9310 |
| sortino_ratio | -3.0954 |
| max_drawdown | 0.9791 |
| cagr | -0.7843 |
| net_avg_win | 15.4840 |
| net_avg_loss | -32.2495 |
| avg_hold_time_bars | 4.4649 |
| exposure | 0.2052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
