# EMA Hourly Continuation — CETUS/USDT P55_200

**Symbol:** CETUS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.9709 |
| net_win_rate | 0.5377 |
| gross_profit_factor | 1.1609 |
| gross_win_rate | 0.5377 |
| sharpe_ratio | -0.1152 |
| sortino_ratio | -0.0283 |
| max_drawdown | 0.2374 |
| cagr | -0.0182 |
| net_avg_win | 96.1518 |
| net_avg_loss | -115.1667 |
| avg_hold_time_bars | 29.9897 |
| exposure | 0.3963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
