# EMA Hourly Continuation — TURBO/USDT P20_200

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.6854 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.5762 |
| sortino_ratio | -0.7187 |
| max_drawdown | 0.5401 |
| cagr | -0.2873 |
| net_avg_win | 71.8134 |
| net_avg_loss | -92.7376 |
| avg_hold_time_bars | 35.9756 |
| exposure | 0.6438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
