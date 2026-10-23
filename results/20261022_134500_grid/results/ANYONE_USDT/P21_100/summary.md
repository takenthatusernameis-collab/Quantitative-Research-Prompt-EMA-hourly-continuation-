# EMA Hourly Continuation — ANYONE/USDT P21_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.6049 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.7783 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -3.9988 |
| sortino_ratio | -1.4420 |
| max_drawdown | 0.7931 |
| cagr | -0.4924 |
| net_avg_win | 46.1630 |
| net_avg_loss | -59.9423 |
| avg_hold_time_bars | 12.9222 |
| exposure | 0.3859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
