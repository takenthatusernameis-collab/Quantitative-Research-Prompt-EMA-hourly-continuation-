# EMA Hourly Continuation — ETN/USDT P89_200

**Symbol:** ETN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.6200 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.7705 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -2.5061 |
| sortino_ratio | -0.6109 |
| max_drawdown | 0.4614 |
| cagr | -0.2450 |
| net_avg_win | 66.7422 |
| net_avg_loss | -84.4201 |
| avg_hold_time_bars | 13.8427 |
| exposure | 0.1865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
