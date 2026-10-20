# EMA Hourly Continuation — UQC/USDT P26_89

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.2311 |
| net_win_rate | 0.2605 |
| gross_profit_factor | 0.4505 |
| gross_win_rate | 0.2997 |
| sharpe_ratio | -8.7726 |
| sortino_ratio | -2.3776 |
| max_drawdown | 0.9671 |
| cagr | -0.7417 |
| net_avg_win | 31.2565 |
| net_avg_loss | -47.6429 |
| avg_hold_time_bars | 29.4846 |
| exposure | 0.4764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
