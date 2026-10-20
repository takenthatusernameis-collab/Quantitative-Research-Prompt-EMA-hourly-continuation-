# EMA Hourly Continuation — CATI/USDT P89_200

**Symbol:** CATI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.5122 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8326 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -4.8408 |
| sortino_ratio | -1.4789 |
| max_drawdown | 0.7812 |
| cagr | -0.5180 |
| net_avg_win | 47.6960 |
| net_avg_loss | -70.5558 |
| avg_hold_time_bars | 8.8095 |
| exposure | 0.1927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
