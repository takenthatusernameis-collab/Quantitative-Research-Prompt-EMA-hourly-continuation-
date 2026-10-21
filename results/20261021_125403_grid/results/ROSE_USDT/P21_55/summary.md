# EMA Hourly Continuation — ROSE/USDT P21_55

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.8134 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0403 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.6268 |
| sortino_ratio | -0.5395 |
| max_drawdown | 0.5471 |
| cagr | -0.2199 |
| net_avg_win | 74.6071 |
| net_avg_loss | -94.5183 |
| avg_hold_time_bars | 8.6273 |
| exposure | 0.2094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
