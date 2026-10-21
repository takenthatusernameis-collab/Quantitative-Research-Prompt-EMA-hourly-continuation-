# EMA Hourly Continuation — ROSE/USDT P50_200

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7066 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0000 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.9600 |
| sortino_ratio | -0.5239 |
| max_drawdown | 0.4767 |
| cagr | -0.2238 |
| net_avg_win | 62.6286 |
| net_avg_loss | -89.1287 |
| avg_hold_time_bars | 26.8338 |
| exposure | 0.4403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
