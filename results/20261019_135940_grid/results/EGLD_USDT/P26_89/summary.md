# EMA Hourly Continuation — EGLD/USDT P26_89

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.6064 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -3.9129 |
| sortino_ratio | -1.4486 |
| max_drawdown | 0.8425 |
| cagr | -0.5034 |
| net_avg_win | 37.6079 |
| net_avg_loss | -59.2261 |
| avg_hold_time_bars | 9.9063 |
| exposure | 0.3125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
