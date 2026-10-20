# EMA Hourly Continuation — ORCA/USDT P21_100

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.6665 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -3.0697 |
| sortino_ratio | -1.0900 |
| max_drawdown | 0.7523 |
| cagr | -0.4039 |
| net_avg_win | 46.7268 |
| net_avg_loss | -67.9273 |
| avg_hold_time_bars | 14.7073 |
| exposure | 0.4225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
