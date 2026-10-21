# EMA Hourly Continuation — GMX/USDT P21_55

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6550 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.4014 |
| sortino_ratio | -1.1936 |
| max_drawdown | 0.7554 |
| cagr | -0.4215 |
| net_avg_win | 49.9400 |
| net_avg_loss | -67.4560 |
| avg_hold_time_bars | 7.9388 |
| exposure | 0.2183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
