# EMA Hourly Continuation — ALPINE/USDT P26_50

**Symbol:** ALPINE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.4126 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.7908 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -8.2634 |
| sortino_ratio | -3.4743 |
| max_drawdown | 0.9868 |
| cagr | -0.8192 |
| net_avg_win | 18.6739 |
| net_avg_loss | -33.1853 |
| avg_hold_time_bars | 5.4595 |
| exposure | 0.2176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
