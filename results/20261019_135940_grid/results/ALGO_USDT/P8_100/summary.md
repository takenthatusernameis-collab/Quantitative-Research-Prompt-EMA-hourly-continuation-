# EMA Hourly Continuation — ALGO/USDT P8_100

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.7133 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0307 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -2.2342 |
| sortino_ratio | -0.7249 |
| max_drawdown | 0.6073 |
| cagr | -0.2960 |
| net_avg_win | 53.3982 |
| net_avg_loss | -77.7019 |
| avg_hold_time_bars | 29.5560 |
| exposure | 0.7201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
