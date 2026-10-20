# EMA Hourly Continuation — KSM/USDT P21_100

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8592 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -4.4183 |
| sortino_ratio | -1.5141 |
| max_drawdown | 0.8475 |
| cagr | -0.5207 |
| net_avg_win | 36.8081 |
| net_avg_loss | -57.4152 |
| avg_hold_time_bars | 16.4565 |
| exposure | 0.4473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
