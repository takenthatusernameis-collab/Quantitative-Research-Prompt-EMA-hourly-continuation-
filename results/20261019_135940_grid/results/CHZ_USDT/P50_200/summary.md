# EMA Hourly Continuation — CHZ/USDT P50_200

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8006 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1414 |
| gross_win_rate | 0.5367 |
| sharpe_ratio | -1.1743 |
| sortino_ratio | -0.3093 |
| max_drawdown | 0.3358 |
| cagr | -0.1359 |
| net_avg_win | 68.5130 |
| net_avg_loss | -95.6754 |
| avg_hold_time_bars | 26.0674 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
