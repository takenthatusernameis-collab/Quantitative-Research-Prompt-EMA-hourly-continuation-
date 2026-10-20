# EMA Hourly Continuation — TURBO/USDT P34_50

**Symbol:** TURBO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 791 |
| net_profit_factor | 0.4993 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.9156 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -8.1833 |
| sortino_ratio | -3.5593 |
| max_drawdown | 0.9779 |
| cagr | -0.8319 |
| net_avg_win | 27.5774 |
| net_avg_loss | -44.5098 |
| avg_hold_time_bars | 2.4475 |
| exposure | 0.1056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
