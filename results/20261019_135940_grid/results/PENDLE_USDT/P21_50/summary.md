# EMA Hourly Continuation — PENDLE/USDT P21_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.5088 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8363 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -6.3736 |
| sortino_ratio | -2.8748 |
| max_drawdown | 0.9685 |
| cagr | -0.7468 |
| net_avg_win | 21.6135 |
| net_avg_loss | -35.5155 |
| avg_hold_time_bars | 4.5918 |
| exposure | 0.2127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
