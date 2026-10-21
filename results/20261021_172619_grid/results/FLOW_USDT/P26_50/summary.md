# EMA Hourly Continuation — FLOW/USDT P26_50

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7665 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.1013 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -1.7563 |
| sortino_ratio | -0.5263 |
| max_drawdown | 0.4854 |
| cagr | -0.2142 |
| net_avg_win | 65.9436 |
| net_avg_loss | -94.3890 |
| avg_hold_time_bars | 6.3380 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
