# EMA Hourly Continuation — MAGIC/USDT P34_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7714 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0222 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.9264 |
| sortino_ratio | -0.5977 |
| max_drawdown | 0.5091 |
| cagr | -0.2406 |
| net_avg_win | 71.6752 |
| net_avg_loss | -93.3083 |
| avg_hold_time_bars | 12.3369 |
| exposure | 0.2630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
