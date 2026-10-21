# EMA Hourly Continuation — EWT/USDT P26_34

**Symbol:** EWT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.7597 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -2.4432 |
| sortino_ratio | -0.4486 |
| max_drawdown | 0.4261 |
| cagr | -0.1878 |
| net_avg_win | 68.1842 |
| net_avg_loss | -94.5119 |
| avg_hold_time_bars | 7.9461 |
| exposure | 0.0603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
