# EMA Hourly Continuation — PHA/USDT P21_100

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.8260 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9927 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.3321 |
| sortino_ratio | -0.4194 |
| max_drawdown | 0.4540 |
| cagr | -0.1773 |
| net_avg_win | 76.3261 |
| net_avg_loss | -91.6455 |
| avg_hold_time_bars | 17.3946 |
| exposure | 0.3827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
