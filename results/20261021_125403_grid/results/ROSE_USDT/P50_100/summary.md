# EMA Hourly Continuation — ROSE/USDT P50_100

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.8042 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0391 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.4038 |
| sortino_ratio | -0.4019 |
| max_drawdown | 0.4079 |
| cagr | -0.1692 |
| net_avg_win | 75.6935 |
| net_avg_loss | -97.4961 |
| avg_hold_time_bars | 9.0378 |
| exposure | 0.1631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
