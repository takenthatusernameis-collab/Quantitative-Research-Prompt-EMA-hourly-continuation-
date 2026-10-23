# EMA Hourly Continuation — ANYONE/USDT P34_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6059 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -4.1234 |
| sortino_ratio | -1.4330 |
| max_drawdown | 0.7890 |
| cagr | -0.4915 |
| net_avg_win | 49.9617 |
| net_avg_loss | -64.7261 |
| avg_hold_time_bars | 9.4051 |
| exposure | 0.2604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
