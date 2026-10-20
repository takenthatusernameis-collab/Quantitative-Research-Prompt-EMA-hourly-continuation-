# EMA Hourly Continuation — ZETA/USDT P26_50

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.5134 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.9248 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -7.0436 |
| sortino_ratio | -3.0625 |
| max_drawdown | 0.9767 |
| cagr | -0.7741 |
| net_avg_win | 23.6836 |
| net_avg_loss | -38.7410 |
| avg_hold_time_bars | 4.0735 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
