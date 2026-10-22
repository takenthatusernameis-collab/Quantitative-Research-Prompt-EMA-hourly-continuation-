# EMA Hourly Continuation — NEAR/USDT P34_100

**Symbol:** NEAR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.6350 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -3.8942 |
| sortino_ratio | -1.3601 |
| max_drawdown | 0.8183 |
| cagr | -0.4782 |
| net_avg_win | 48.2843 |
| net_avg_loss | -68.0565 |
| avg_hold_time_bars | 9.3550 |
| exposure | 0.2611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
