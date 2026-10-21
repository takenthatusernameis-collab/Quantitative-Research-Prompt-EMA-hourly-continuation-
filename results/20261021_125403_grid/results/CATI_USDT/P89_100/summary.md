# EMA Hourly Continuation — CATI/USDT P89_100

**Symbol:** CATI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 94 |
| net_profit_factor | 0.4702 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.6728 |
| gross_win_rate | 0.4043 |
| sharpe_ratio | -2.4196 |
| sortino_ratio | -0.3664 |
| max_drawdown | 0.3068 |
| cagr | -0.1552 |
| net_avg_win | 69.1855 |
| net_avg_loss | -99.8426 |
| avg_hold_time_bars | 10.7766 |
| exposure | 0.0555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
