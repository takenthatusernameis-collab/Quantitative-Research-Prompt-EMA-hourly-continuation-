# EMA Hourly Continuation — EWT/USDT P26_89

**Symbol:** EWT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.4979 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7714 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -5.9928 |
| sortino_ratio | -2.2277 |
| max_drawdown | 0.9411 |
| cagr | -0.6665 |
| net_avg_win | 30.8558 |
| net_avg_loss | -45.9444 |
| avg_hold_time_bars | 8.2277 |
| exposure | 0.2644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
