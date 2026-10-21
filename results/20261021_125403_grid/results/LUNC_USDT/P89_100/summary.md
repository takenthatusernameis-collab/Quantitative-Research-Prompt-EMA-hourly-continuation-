# EMA Hourly Continuation — LUNC/USDT P89_100

**Symbol:** LUNC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 96 |
| net_profit_factor | 0.7299 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0746 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.9171 |
| sortino_ratio | -0.1297 |
| max_drawdown | 0.1506 |
| cagr | -0.0574 |
| net_avg_win | 74.6002 |
| net_avg_loss | -111.0868 |
| avg_hold_time_bars | 6.0312 |
| exposure | 0.0263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
