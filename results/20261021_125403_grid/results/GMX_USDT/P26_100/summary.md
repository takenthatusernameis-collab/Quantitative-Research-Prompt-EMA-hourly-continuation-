# EMA Hourly Continuation — GMX/USDT P26_100

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6894 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -2.8899 |
| sortino_ratio | -0.9214 |
| max_drawdown | 0.6665 |
| cagr | -0.3450 |
| net_avg_win | 62.0700 |
| net_avg_loss | -78.3210 |
| avg_hold_time_bars | 14.0398 |
| exposure | 0.3210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
