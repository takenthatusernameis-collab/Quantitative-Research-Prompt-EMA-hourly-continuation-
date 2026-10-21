# EMA Hourly Continuation — PHA/USDT P26_100

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7632 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9267 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.8204 |
| sortino_ratio | -0.5622 |
| max_drawdown | 0.5003 |
| cagr | -0.2285 |
| net_avg_win | 68.2445 |
| net_avg_loss | -83.1687 |
| avg_hold_time_bars | 14.4563 |
| exposure | 0.3082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
