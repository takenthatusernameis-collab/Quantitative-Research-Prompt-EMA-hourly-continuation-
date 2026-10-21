# EMA Hourly Continuation — FLR/USDT P8_12

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.4701 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7082 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -3.5988 |
| sortino_ratio | -0.8650 |
| max_drawdown | 0.6378 |
| cagr | -0.3286 |
| net_avg_win | 45.9833 |
| net_avg_loss | -74.5811 |
| avg_hold_time_bars | 4.2305 |
| exposure | 0.0542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
