# EMA Hourly Continuation — MOODENG/USDT P34_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.2563 |
| sortino_ratio | -0.6104 |
| max_drawdown | 0.4630 |
| cagr | -0.2448 |
| net_avg_win | 72.9393 |
| net_avg_loss | -95.3334 |
| avg_hold_time_bars | 5.9593 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
