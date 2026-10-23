# EMA Hourly Continuation — MOODENG/USDT P8_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7197 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.8638 |
| sortino_ratio | -0.9900 |
| max_drawdown | 0.6432 |
| cagr | -0.3742 |
| net_avg_win | 67.4367 |
| net_avg_loss | -85.7085 |
| avg_hold_time_bars | 25.0202 |
| exposure | 0.6839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
