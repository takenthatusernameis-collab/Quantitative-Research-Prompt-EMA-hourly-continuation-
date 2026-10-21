# EMA Hourly Continuation — DYDX/USDT P8_200

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.9154 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0674 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -0.3614 |
| sortino_ratio | -0.0761 |
| max_drawdown | 0.1487 |
| cagr | -0.0370 |
| net_avg_win | 87.3437 |
| net_avg_loss | -103.7556 |
| avg_hold_time_bars | 85.7070 |
| exposure | 0.8376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
