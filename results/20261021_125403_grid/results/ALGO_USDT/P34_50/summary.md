# EMA Hourly Continuation — ALGO/USDT P34_50

**Symbol:** ALGO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.8410 |
| net_win_rate | 0.5500 |
| gross_profit_factor | 1.2123 |
| gross_win_rate | 0.5500 |
| sharpe_ratio | -0.7589 |
| sortino_ratio | -0.1636 |
| max_drawdown | 0.2134 |
| cagr | -0.0726 |
| net_avg_win | 75.3853 |
| net_avg_loss | -109.5525 |
| avg_hold_time_bars | 4.7500 |
| exposure | 0.0475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
