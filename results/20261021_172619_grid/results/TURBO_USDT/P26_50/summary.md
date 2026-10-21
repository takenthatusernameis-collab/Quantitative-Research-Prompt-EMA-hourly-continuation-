# EMA Hourly Continuation — TURBO/USDT P26_50

**Symbol:** TURBO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7765 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0023 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6054 |
| sortino_ratio | -0.4567 |
| max_drawdown | 0.3966 |
| cagr | -0.1892 |
| net_avg_win | 75.2388 |
| net_avg_loss | -96.9006 |
| avg_hold_time_bars | 6.3963 |
| exposure | 0.1145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
