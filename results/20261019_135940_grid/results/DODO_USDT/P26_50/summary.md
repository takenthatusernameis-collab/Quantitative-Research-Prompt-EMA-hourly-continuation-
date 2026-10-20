# EMA Hourly Continuation — DODO/USDT P26_50

**Symbol:** DODO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.5056 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -8.6821 |
| sortino_ratio | -3.9538 |
| max_drawdown | 0.9933 |
| cagr | -0.8581 |
| net_avg_win | 22.7676 |
| net_avg_loss | -33.4140 |
| avg_hold_time_bars | 3.6762 |
| exposure | 0.1742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
