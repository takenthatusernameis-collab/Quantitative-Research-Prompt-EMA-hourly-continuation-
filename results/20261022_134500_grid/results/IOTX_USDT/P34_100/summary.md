# EMA Hourly Continuation — IOTX/USDT P34_100

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5824 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -4.9061 |
| sortino_ratio | -1.7809 |
| max_drawdown | 0.8934 |
| cagr | -0.5812 |
| net_avg_win | 39.8005 |
| net_avg_loss | -58.8745 |
| avg_hold_time_bars | 8.9524 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
