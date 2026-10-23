# EMA Hourly Continuation — ANKR/USDT P34_100

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.5128 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.8600 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -6.1066 |
| sortino_ratio | -2.2201 |
| max_drawdown | 0.9357 |
| cagr | -0.6625 |
| net_avg_win | 34.1598 |
| net_avg_loss | -50.3524 |
| avg_hold_time_bars | 10.2975 |
| exposure | 0.3131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
