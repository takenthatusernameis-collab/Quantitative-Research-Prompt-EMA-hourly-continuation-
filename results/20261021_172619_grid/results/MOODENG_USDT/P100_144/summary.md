# EMA Hourly Continuation — MOODENG/USDT P100_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.8667 |
| net_win_rate | 0.5297 |
| gross_profit_factor | 1.1162 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -0.6549 |
| sortino_ratio | -0.1482 |
| max_drawdown | 0.1567 |
| cagr | -0.0674 |
| net_avg_win | 81.4180 |
| net_avg_loss | -105.8072 |
| avg_hold_time_bars | 6.5545 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
