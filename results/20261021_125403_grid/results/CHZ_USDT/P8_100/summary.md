# EMA Hourly Continuation — CHZ/USDT P8_100

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.9013 |
| net_win_rate | 0.5235 |
| gross_profit_factor | 1.0999 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -0.7097 |
| sortino_ratio | -0.2259 |
| max_drawdown | 0.3433 |
| cagr | -0.1034 |
| net_avg_win | 85.5369 |
| net_avg_loss | -104.2679 |
| avg_hold_time_bars | 29.1084 |
| exposure | 0.6470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
