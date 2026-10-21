# EMA Hourly Continuation — ANKR/USDT P20_89

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6574 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4491 |
| sharpe_ratio | -3.4546 |
| sortino_ratio | -1.1200 |
| max_drawdown | 0.7352 |
| cagr | -0.4036 |
| net_avg_win | 59.6211 |
| net_avg_loss | -73.9387 |
| avg_hold_time_bars | 17.6353 |
| exposure | 0.4176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
