# EMA Hourly Continuation — COMP/USDT P100_200

**Symbol:** COMP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.4273 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8372 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -4.7769 |
| sortino_ratio | -1.3785 |
| max_drawdown | 0.8197 |
| cagr | -0.4941 |
| net_avg_win | 33.0491 |
| net_avg_loss | -61.1431 |
| avg_hold_time_bars | 8.3986 |
| exposure | 0.1600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
