# EMA Hourly Continuation — ROSE/USDT P26_200

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8552 |
| net_win_rate | 0.5293 |
| gross_profit_factor | 1.1121 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -0.9351 |
| sortino_ratio | -0.2598 |
| max_drawdown | 0.3215 |
| cagr | -0.1157 |
| net_avg_win | 78.8460 |
| net_avg_loss | -103.6567 |
| avg_hold_time_bars | 34.6702 |
| exposure | 0.5925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
