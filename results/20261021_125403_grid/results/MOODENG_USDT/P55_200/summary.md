# EMA Hourly Continuation — MOODENG/USDT P55_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.8187 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.0274 |
| sortino_ratio | -0.2438 |
| max_drawdown | 0.2514 |
| cagr | -0.1078 |
| net_avg_win | 85.2788 |
| net_avg_loss | -98.8242 |
| avg_hold_time_bars | 31.3465 |
| exposure | 0.3955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
