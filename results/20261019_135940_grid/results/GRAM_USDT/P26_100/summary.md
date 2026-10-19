# EMA Hourly Continuation — GRAM/USDT P26_100

**Symbol:** GRAM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.4310 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8870 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -6.2729 |
| sortino_ratio | -2.3343 |
| max_drawdown | 0.9510 |
| cagr | -0.6900 |
| net_avg_win | 22.2776 |
| net_avg_loss | -42.4631 |
| avg_hold_time_bars | 10.4090 |
| exposure | 0.3378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
