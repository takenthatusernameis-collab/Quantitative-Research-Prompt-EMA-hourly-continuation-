# EMA Hourly Continuation — OSMO/USDT P89_100

**Symbol:** OSMO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.6235 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9992 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.8997 |
| sortino_ratio | -0.3542 |
| max_drawdown | 0.3476 |
| cagr | -0.1498 |
| net_avg_win | 66.7815 |
| net_avg_loss | -105.8328 |
| avg_hold_time_bars | 4.6407 |
| exposure | 0.0352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
