# EMA Hourly Continuation — ROSE/USDT P21_50

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.8048 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0461 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.7263 |
| sortino_ratio | -0.5673 |
| max_drawdown | 0.5578 |
| cagr | -0.2292 |
| net_avg_win | 74.3935 |
| net_avg_loss | -95.3013 |
| avg_hold_time_bars | 7.4466 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
