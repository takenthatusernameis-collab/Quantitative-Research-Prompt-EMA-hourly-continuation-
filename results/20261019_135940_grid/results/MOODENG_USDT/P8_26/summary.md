# EMA Hourly Continuation — MOODENG/USDT P8_26

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.5844 |
| net_win_rate | 0.4461 |
| gross_profit_factor | 0.8654 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -8.5606 |
| sortino_ratio | -4.6141 |
| max_drawdown | 0.9918 |
| cagr | -0.8963 |
| net_avg_win | 25.7029 |
| net_avg_loss | -35.4202 |
| avg_hold_time_bars | 4.3778 |
| exposure | 0.2943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
