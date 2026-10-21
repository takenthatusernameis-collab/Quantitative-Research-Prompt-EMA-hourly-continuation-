# EMA Hourly Continuation — POL/USDT P8_12

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.5145 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.7424 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -2.6142 |
| sortino_ratio | -0.5553 |
| max_drawdown | 0.4977 |
| cagr | -0.2246 |
| net_avg_win | 50.5252 |
| net_avg_loss | -79.6965 |
| avg_hold_time_bars | 4.2398 |
| exposure | 0.0426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
