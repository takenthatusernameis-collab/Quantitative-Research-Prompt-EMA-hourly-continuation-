# EMA Hourly Continuation — RSR/USDT P21_34

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1088 |
| net_profit_factor | 0.4071 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8135 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -9.1516 |
| sortino_ratio | -4.2852 |
| max_drawdown | 0.9952 |
| cagr | -0.8792 |
| net_avg_win | 14.5651 |
| net_avg_loss | -27.1107 |
| avg_hold_time_bars | 2.7812 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
