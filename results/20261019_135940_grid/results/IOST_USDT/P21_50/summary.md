# EMA Hourly Continuation — IOST/USDT P21_50

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.4329 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8465 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -7.7908 |
| sortino_ratio | -3.3598 |
| max_drawdown | 0.9855 |
| cagr | -0.8128 |
| net_avg_win | 17.9868 |
| net_avg_loss | -33.3392 |
| avg_hold_time_bars | 5.3429 |
| exposure | 0.2280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
