# EMA Hourly Continuation — LUNC/USDT P34_200

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8382 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -3.7955 |
| sortino_ratio | -1.1161 |
| max_drawdown | 0.7577 |
| cagr | -0.4184 |
| net_avg_win | 44.2691 |
| net_avg_loss | -67.3117 |
| avg_hold_time_bars | 23.4683 |
| exposure | 0.4715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
