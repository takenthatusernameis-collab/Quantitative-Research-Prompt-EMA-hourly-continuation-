# EMA Hourly Continuation — ZBCN/USDT P8_21

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.9209 |
| net_win_rate | 0.5352 |
| gross_profit_factor | 1.1416 |
| gross_win_rate | 0.5352 |
| sharpe_ratio | -0.4789 |
| sortino_ratio | -0.1442 |
| max_drawdown | 0.2386 |
| cagr | -0.0692 |
| net_avg_win | 82.8418 |
| net_avg_loss | -103.5838 |
| avg_hold_time_bars | 6.3568 |
| exposure | 0.1253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
