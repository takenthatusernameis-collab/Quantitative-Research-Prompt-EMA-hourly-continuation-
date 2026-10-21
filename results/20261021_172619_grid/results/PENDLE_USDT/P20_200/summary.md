# EMA Hourly Continuation — PENDLE/USDT P20_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7556 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -1.3281 |
| sortino_ratio | -0.2846 |
| max_drawdown | 0.3453 |
| cagr | -0.1233 |
| net_avg_win | 82.0824 |
| net_avg_loss | -94.3837 |
| avg_hold_time_bars | 68.5307 |
| exposure | 0.7102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
