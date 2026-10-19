# EMA Hourly Continuation — LINK/USDT P34_200

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6073 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9627 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.8415 |
| sortino_ratio | -0.7864 |
| max_drawdown | 0.6389 |
| cagr | -0.3177 |
| net_avg_win | 49.4581 |
| net_avg_loss | -77.8078 |
| avg_hold_time_bars | 26.0709 |
| exposure | 0.4681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
