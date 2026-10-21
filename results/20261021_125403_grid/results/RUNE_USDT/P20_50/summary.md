# EMA Hourly Continuation — RUNE/USDT P20_50

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7094 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9728 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.4847 |
| sortino_ratio | -0.7875 |
| max_drawdown | 0.5974 |
| cagr | -0.3017 |
| net_avg_win | 60.1776 |
| net_avg_loss | -82.4398 |
| avg_hold_time_bars | 7.8119 |
| exposure | 0.1736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
