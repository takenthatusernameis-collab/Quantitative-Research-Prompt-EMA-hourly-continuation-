# EMA Hourly Continuation — MOODENG/USDT P26_34

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 181 |
| net_profit_factor | 0.5907 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8029 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -2.5504 |
| sortino_ratio | -0.5376 |
| max_drawdown | 0.4201 |
| cagr | -0.2213 |
| net_avg_win | 72.7145 |
| net_avg_loss | -97.5032 |
| avg_hold_time_bars | 4.2707 |
| exposure | 0.0428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
