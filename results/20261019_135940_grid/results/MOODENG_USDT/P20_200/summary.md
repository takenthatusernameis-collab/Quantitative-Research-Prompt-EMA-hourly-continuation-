# EMA Hourly Continuation — MOODENG/USDT P20_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.7587 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 1.0257 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.5152 |
| sortino_ratio | -0.3643 |
| max_drawdown | 0.3304 |
| cagr | -0.1564 |
| net_avg_win | 80.2037 |
| net_avg_loss | -102.1921 |
| avg_hold_time_bars | 54.7500 |
| exposure | 0.7149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
