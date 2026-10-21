# EMA Hourly Continuation — ALGO/USDT P21_50

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.7648 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0419 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -1.7676 |
| sortino_ratio | -0.5604 |
| max_drawdown | 0.4930 |
| cagr | -0.2262 |
| net_avg_win | 62.0062 |
| net_avg_loss | -85.5392 |
| avg_hold_time_bars | 6.6412 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
