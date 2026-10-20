# EMA Hourly Continuation — CYBER/USDT P21_55

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.5471 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -7.0358 |
| sortino_ratio | -2.9817 |
| max_drawdown | 0.9746 |
| cagr | -0.7675 |
| net_avg_win | 29.7199 |
| net_avg_loss | -41.9351 |
| avg_hold_time_bars | 6.3245 |
| exposure | 0.2613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
