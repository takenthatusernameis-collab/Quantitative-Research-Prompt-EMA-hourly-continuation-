# EMA Hourly Continuation — DYDX/USDT P50_100

**Symbol:** DYDX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6754 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.8842 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.2464 |
| sortino_ratio | -0.6324 |
| max_drawdown | 0.5313 |
| cagr | -0.2516 |
| net_avg_win | 58.1482 |
| net_avg_loss | -78.0761 |
| avg_hold_time_bars | 8.0051 |
| exposure | 0.1415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
