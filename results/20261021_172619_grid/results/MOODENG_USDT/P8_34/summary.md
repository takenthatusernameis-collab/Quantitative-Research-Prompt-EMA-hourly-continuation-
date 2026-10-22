# EMA Hourly Continuation — MOODENG/USDT P8_34

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.8782 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.1046 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -1.2049 |
| sortino_ratio | -0.4617 |
| max_drawdown | 0.4375 |
| cagr | -0.1961 |
| net_avg_win | 85.7282 |
| net_avg_loss | -106.7127 |
| avg_hold_time_bars | 9.4195 |
| exposure | 0.3044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
