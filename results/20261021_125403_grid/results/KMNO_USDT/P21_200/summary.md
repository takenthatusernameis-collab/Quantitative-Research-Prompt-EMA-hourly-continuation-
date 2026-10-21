# EMA Hourly Continuation — KMNO/USDT P21_200

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7813 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9268 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -1.3809 |
| sortino_ratio | -0.3451 |
| max_drawdown | 0.3406 |
| cagr | -0.1484 |
| net_avg_win | 80.2163 |
| net_avg_loss | -94.8690 |
| avg_hold_time_bars | 41.5461 |
| exposure | 0.5831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
