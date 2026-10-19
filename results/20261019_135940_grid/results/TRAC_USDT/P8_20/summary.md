# EMA Hourly Continuation — TRAC/USDT P8_20

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1347 |
| net_profit_factor | 0.4337 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.8707 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -10.5285 |
| sortino_ratio | -5.4183 |
| max_drawdown | 0.9990 |
| cagr | -0.9366 |
| net_avg_win | 13.3302 |
| net_avg_loss | -22.8224 |
| avg_hold_time_bars | 3.9881 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
