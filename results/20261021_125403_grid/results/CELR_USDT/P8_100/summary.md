# EMA Hourly Continuation — CELR/USDT P8_100

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7704 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -2.0035 |
| sortino_ratio | -0.6393 |
| max_drawdown | 0.5414 |
| cagr | -0.2561 |
| net_avg_win | 72.3035 |
| net_avg_loss | -88.4200 |
| avg_hold_time_bars | 29.0954 |
| exposure | 0.6622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
