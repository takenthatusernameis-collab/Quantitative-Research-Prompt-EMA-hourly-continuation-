# EMA Hourly Continuation — STRK/USDT P26_50

**Symbol:** STRK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.5160 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.9269 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -7.0280 |
| sortino_ratio | -3.0428 |
| max_drawdown | 0.9752 |
| cagr | -0.7702 |
| net_avg_win | 24.5714 |
| net_avg_loss | -39.2683 |
| avg_hold_time_bars | 3.4573 |
| exposure | 0.1471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
