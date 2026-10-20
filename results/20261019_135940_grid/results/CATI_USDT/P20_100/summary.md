# EMA Hourly Continuation — CATI/USDT P20_100

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.5620 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -5.3767 |
| sortino_ratio | -2.0503 |
| max_drawdown | 0.8803 |
| cagr | -0.6242 |
| net_avg_win | 41.3238 |
| net_avg_loss | -58.9150 |
| avg_hold_time_bars | 13.6211 |
| exposure | 0.4532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
