# EMA Hourly Continuation — STRK/USDT P12_100

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.8260 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -1.2044 |
| sortino_ratio | -0.3602 |
| max_drawdown | 0.3954 |
| cagr | -0.1549 |
| net_avg_win | 75.0833 |
| net_avg_loss | -90.0685 |
| avg_hold_time_bars | 29.2283 |
| exposure | 0.5819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
