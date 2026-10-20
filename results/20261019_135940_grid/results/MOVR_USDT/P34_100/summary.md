# EMA Hourly Continuation — MOVR/USDT P34_100

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.4829 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.7837 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -5.6299 |
| sortino_ratio | -2.0654 |
| max_drawdown | 0.9257 |
| cagr | -0.6303 |
| net_avg_win | 28.9572 |
| net_avg_loss | -45.8645 |
| avg_hold_time_bars | 8.5564 |
| exposure | 0.2656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
