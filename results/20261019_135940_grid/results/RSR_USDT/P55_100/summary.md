# EMA Hourly Continuation — RSR/USDT P55_100

**Symbol:** RSR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5674 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.8809 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -4.1410 |
| sortino_ratio | -1.4743 |
| max_drawdown | 0.8320 |
| cagr | -0.5034 |
| net_avg_win | 36.3097 |
| net_avg_loss | -57.1114 |
| avg_hold_time_bars | 5.0804 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
