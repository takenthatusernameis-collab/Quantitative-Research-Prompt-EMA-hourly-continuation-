# EMA Hourly Continuation — KAS/USDT P26_100

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.8486 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0724 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -1.0873 |
| sortino_ratio | -0.3232 |
| max_drawdown | 0.3548 |
| cagr | -0.1398 |
| net_avg_win | 79.8298 |
| net_avg_loss | -100.9279 |
| avg_hold_time_bars | 14.7845 |
| exposure | 0.2870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
