# EMA Hourly Continuation — ASTR/USDT P20_50

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.5098 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -6.4568 |
| sortino_ratio | -2.7292 |
| max_drawdown | 0.9671 |
| cagr | -0.7384 |
| net_avg_win | 23.3125 |
| net_avg_loss | -41.4033 |
| avg_hold_time_bars | 5.5612 |
| exposure | 0.2283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
