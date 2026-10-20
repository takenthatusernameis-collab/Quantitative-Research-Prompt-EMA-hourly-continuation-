# EMA Hourly Continuation — SWFTC/USDT P8_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 942 |
| net_profit_factor | 0.5625 |
| net_win_rate | 0.4363 |
| gross_profit_factor | 0.8593 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -6.5220 |
| sortino_ratio | -2.7959 |
| max_drawdown | 0.9687 |
| cagr | -0.7474 |
| net_avg_win | 30.2995 |
| net_avg_loss | -41.6900 |
| avg_hold_time_bars | 12.4023 |
| exposure | 0.5310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
