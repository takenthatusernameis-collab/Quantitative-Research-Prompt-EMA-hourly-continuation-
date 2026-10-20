# EMA Hourly Continuation — MOODENG/USDT P34_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.5252 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8449 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -6.4658 |
| sortino_ratio | -2.7842 |
| max_drawdown | 0.9361 |
| cagr | -0.7363 |
| net_avg_win | 29.9238 |
| net_avg_loss | -47.6193 |
| avg_hold_time_bars | 3.3079 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
