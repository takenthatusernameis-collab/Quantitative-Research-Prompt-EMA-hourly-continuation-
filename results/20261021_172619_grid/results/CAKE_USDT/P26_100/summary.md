# EMA Hourly Continuation — CAKE/USDT P26_100

**Symbol:** CAKE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.8588 |
| net_win_rate | 0.5340 |
| gross_profit_factor | 1.1473 |
| gross_win_rate | 0.5363 |
| sharpe_ratio | -0.9814 |
| sortino_ratio | -0.2925 |
| max_drawdown | 0.3710 |
| cagr | -0.1279 |
| net_avg_win | 77.5663 |
| net_avg_loss | -103.4873 |
| avg_hold_time_bars | 18.9133 |
| exposure | 0.3671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
