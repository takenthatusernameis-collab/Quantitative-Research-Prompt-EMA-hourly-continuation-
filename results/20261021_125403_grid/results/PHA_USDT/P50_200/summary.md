# EMA Hourly Continuation — PHA/USDT P50_200

**Symbol:** PHA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7226 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -1.8313 |
| sortino_ratio | -0.4616 |
| max_drawdown | 0.4488 |
| cagr | -0.1922 |
| net_avg_win | 74.5542 |
| net_avg_loss | -87.4864 |
| avg_hold_time_bars | 23.3133 |
| exposure | 0.3349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
