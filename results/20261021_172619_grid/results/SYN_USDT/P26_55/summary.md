# EMA Hourly Continuation — SYN/USDT P26_55

**Symbol:** SYN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7234 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9447 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.2339 |
| sortino_ratio | -0.7187 |
| max_drawdown | 0.5878 |
| cagr | -0.2810 |
| net_avg_win | 59.6487 |
| net_avg_loss | -78.6332 |
| avg_hold_time_bars | 6.9526 |
| exposure | 0.1599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
