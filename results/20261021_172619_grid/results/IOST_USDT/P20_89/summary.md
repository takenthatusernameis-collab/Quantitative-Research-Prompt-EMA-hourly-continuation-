# EMA Hourly Continuation — IOST/USDT P20_89

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.8201 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1025 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -1.3809 |
| sortino_ratio | -0.4553 |
| max_drawdown | 0.4329 |
| cagr | -0.1906 |
| net_avg_win | 68.0371 |
| net_avg_loss | -92.3336 |
| avg_hold_time_bars | 14.9847 |
| exposure | 0.3569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
