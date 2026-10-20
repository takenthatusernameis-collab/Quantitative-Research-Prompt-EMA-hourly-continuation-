# EMA Hourly Continuation — SATS/USDT P26_100

**Symbol:** SATS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9000 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -3.7296 |
| sortino_ratio | -1.3191 |
| max_drawdown | 0.7974 |
| cagr | -0.4623 |
| net_avg_win | 46.7755 |
| net_avg_loss | -63.4363 |
| avg_hold_time_bars | 10.9130 |
| exposure | 0.3121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
