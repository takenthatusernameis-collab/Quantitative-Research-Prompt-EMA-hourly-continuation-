# EMA Hourly Continuation — JTO/USDT P21_100

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6993 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -3.0360 |
| sortino_ratio | -1.0958 |
| max_drawdown | 0.7445 |
| cagr | -0.4021 |
| net_avg_win | 54.0604 |
| net_avg_loss | -71.1451 |
| avg_hold_time_bars | 13.7849 |
| exposure | 0.4079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
