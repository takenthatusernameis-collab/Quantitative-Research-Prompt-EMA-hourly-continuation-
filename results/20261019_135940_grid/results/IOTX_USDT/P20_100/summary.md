# EMA Hourly Continuation — IOTX/USDT P20_100

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.5854 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -4.6700 |
| sortino_ratio | -1.7668 |
| max_drawdown | 0.8907 |
| cagr | -0.5758 |
| net_avg_win | 36.4887 |
| net_avg_loss | -54.9445 |
| avg_hold_time_bars | 11.9616 |
| exposure | 0.3969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
