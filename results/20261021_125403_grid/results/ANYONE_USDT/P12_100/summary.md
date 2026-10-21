# EMA Hourly Continuation — ANYONE/USDT P12_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8108 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9255 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -1.5243 |
| sortino_ratio | -0.5059 |
| max_drawdown | 0.4462 |
| cagr | -0.2105 |
| net_avg_win | 75.1075 |
| net_avg_loss | -86.4122 |
| avg_hold_time_bars | 20.3620 |
| exposure | 0.5031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
