# EMA Hourly Continuation — MOODENG/USDT P21_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7870 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -1.7410 |
| sortino_ratio | -0.5377 |
| max_drawdown | 0.4373 |
| cagr | -0.2206 |
| net_avg_win | 80.2823 |
| net_avg_loss | -93.4304 |
| avg_hold_time_bars | 18.5917 |
| exposure | 0.3981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
