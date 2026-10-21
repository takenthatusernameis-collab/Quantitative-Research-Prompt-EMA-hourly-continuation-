# EMA Hourly Continuation — CAKE/USDT P12_34

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.6687 |
| sortino_ratio | -0.8978 |
| max_drawdown | 0.6600 |
| cagr | -0.3375 |
| net_avg_win | 63.4433 |
| net_avg_loss | -86.6453 |
| avg_hold_time_bars | 8.2769 |
| exposure | 0.2065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
