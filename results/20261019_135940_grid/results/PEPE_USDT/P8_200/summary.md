# EMA Hourly Continuation — PEPE/USDT P8_200

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7397 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -1.7377 |
| sortino_ratio | -0.4814 |
| max_drawdown | 0.4490 |
| cagr | -0.2015 |
| net_avg_win | 63.5518 |
| net_avg_loss | -89.1531 |
| avg_hold_time_bars | 46.3113 |
| exposure | 0.7978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
