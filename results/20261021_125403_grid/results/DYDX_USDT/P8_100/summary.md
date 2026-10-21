# EMA Hourly Continuation — DYDX/USDT P8_100

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8264 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9916 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1692 |
| sortino_ratio | -0.3360 |
| max_drawdown | 0.3554 |
| cagr | -0.1451 |
| net_avg_win | 76.7026 |
| net_avg_loss | -92.8141 |
| avg_hold_time_bars | 38.4282 |
| exposure | 0.7057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
