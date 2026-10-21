# EMA Hourly Continuation — TRAC/USDT P20_50

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7645 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.7580 |
| sortino_ratio | -0.5545 |
| max_drawdown | 0.4990 |
| cagr | -0.2243 |
| net_avg_win | 62.7538 |
| net_avg_loss | -83.7975 |
| avg_hold_time_bars | 9.5859 |
| exposure | 0.2105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
