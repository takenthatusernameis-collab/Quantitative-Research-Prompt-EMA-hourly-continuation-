# EMA Hourly Continuation — RUNE/USDT P8_20

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6614 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9370 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -3.0827 |
| sortino_ratio | -0.9762 |
| max_drawdown | 0.6813 |
| cagr | -0.3612 |
| net_avg_win | 56.1478 |
| net_avg_loss | -78.5427 |
| avg_hold_time_bars | 5.2658 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
