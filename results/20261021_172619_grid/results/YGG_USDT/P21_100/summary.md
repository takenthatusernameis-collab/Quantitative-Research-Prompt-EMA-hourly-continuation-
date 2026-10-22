# EMA Hourly Continuation — YGG/USDT P21_100

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8134 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9975 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -1.6334 |
| sortino_ratio | -0.5248 |
| max_drawdown | 0.5275 |
| cagr | -0.2155 |
| net_avg_win | 79.5287 |
| net_avg_loss | -95.8605 |
| avg_hold_time_bars | 17.3570 |
| exposure | 0.3982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
