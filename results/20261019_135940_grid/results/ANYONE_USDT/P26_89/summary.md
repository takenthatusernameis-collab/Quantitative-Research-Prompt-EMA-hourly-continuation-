# EMA Hourly Continuation — ANYONE/USDT P26_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.5854 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.7784 |
| gross_win_rate | 0.4309 |
| sharpe_ratio | -4.7288 |
| sortino_ratio | -1.7114 |
| max_drawdown | 0.8447 |
| cagr | -0.5582 |
| net_avg_win | 46.6207 |
| net_avg_loss | -58.6952 |
| avg_hold_time_bars | 10.3794 |
| exposure | 0.3152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
