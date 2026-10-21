# EMA Hourly Continuation — DYDX/USDT P20_200

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8493 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9882 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8543 |
| sortino_ratio | -0.2100 |
| max_drawdown | 0.2565 |
| cagr | -0.0942 |
| net_avg_win | 83.7548 |
| net_avg_loss | -98.6140 |
| avg_hold_time_bars | 48.2635 |
| exposure | 0.6494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
