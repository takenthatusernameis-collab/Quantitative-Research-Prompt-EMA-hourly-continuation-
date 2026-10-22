# EMA Hourly Continuation — DASH/USDT P50_200

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.4268 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.7810 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -4.6861 |
| sortino_ratio | -1.3481 |
| max_drawdown | 0.8279 |
| cagr | -0.4938 |
| net_avg_win | 32.4415 |
| net_avg_loss | -59.2942 |
| avg_hold_time_bars | 18.7110 |
| exposure | 0.3649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
