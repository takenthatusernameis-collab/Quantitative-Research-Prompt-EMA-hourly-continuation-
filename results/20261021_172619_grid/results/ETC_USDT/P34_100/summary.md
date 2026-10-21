# EMA Hourly Continuation — ETC/USDT P34_100

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9659 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.3081 |
| sortino_ratio | -0.6565 |
| max_drawdown | 0.5441 |
| cagr | -0.2592 |
| net_avg_win | 59.4757 |
| net_avg_loss | -84.1552 |
| avg_hold_time_bars | 14.2995 |
| exposure | 0.2561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
