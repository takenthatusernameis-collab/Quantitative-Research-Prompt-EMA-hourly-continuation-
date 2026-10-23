# EMA Hourly Continuation — ANKR/USDT P34_200

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6222 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -3.3600 |
| sortino_ratio | -0.9301 |
| max_drawdown | 0.6947 |
| cagr | -0.3700 |
| net_avg_win | 61.1351 |
| net_avg_loss | -86.1434 |
| avg_hold_time_bars | 29.2399 |
| exposure | 0.5263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
