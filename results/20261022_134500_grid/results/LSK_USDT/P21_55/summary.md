# EMA Hourly Continuation — LSK/USDT P21_55

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.5352 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -5.6973 |
| sortino_ratio | -2.2762 |
| max_drawdown | 0.9376 |
| cagr | -0.6620 |
| net_avg_win | 29.3135 |
| net_avg_loss | -46.7491 |
| avg_hold_time_bars | 6.7365 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
