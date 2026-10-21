# EMA Hourly Continuation — PENDLE/USDT P8_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.9371 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0584 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -0.2857 |
| sortino_ratio | -0.0638 |
| max_drawdown | 0.2306 |
| cagr | -0.0322 |
| net_avg_win | 94.7276 |
| net_avg_loss | -107.1392 |
| avg_hold_time_bars | 73.7344 |
| exposure | 0.8077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
