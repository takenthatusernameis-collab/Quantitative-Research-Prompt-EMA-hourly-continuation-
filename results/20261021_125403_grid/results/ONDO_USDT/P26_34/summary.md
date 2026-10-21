# EMA Hourly Continuation — ONDO/USDT P26_34

**Symbol:** ONDO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 0.8108 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0888 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.7945 |
| sortino_ratio | -0.1375 |
| max_drawdown | 0.2071 |
| cagr | -0.0614 |
| net_avg_win | 84.1070 |
| net_avg_loss | -112.7547 |
| avg_hold_time_bars | 6.0486 |
| exposure | 0.0396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
