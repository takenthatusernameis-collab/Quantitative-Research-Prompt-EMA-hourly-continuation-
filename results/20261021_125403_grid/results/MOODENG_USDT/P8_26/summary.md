# EMA Hourly Continuation — MOODENG/USDT P8_26

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7464 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -2.5077 |
| sortino_ratio | -0.9116 |
| max_drawdown | 0.6311 |
| cagr | -0.3432 |
| net_avg_win | 66.1679 |
| net_avg_loss | -83.1655 |
| avg_hold_time_bars | 7.9850 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
