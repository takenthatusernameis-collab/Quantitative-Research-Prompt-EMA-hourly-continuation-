# EMA Hourly Continuation — MOODENG/USDT P21_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.7667 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 1.0332 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.4330 |
| sortino_ratio | -0.3411 |
| max_drawdown | 0.3223 |
| cagr | -0.1472 |
| net_avg_win | 80.6900 |
| net_avg_loss | -102.5449 |
| avg_hold_time_bars | 55.7316 |
| exposure | 0.7123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
