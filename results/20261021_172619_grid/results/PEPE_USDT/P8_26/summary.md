# EMA Hourly Continuation — PEPE/USDT P8_26

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7665 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9727 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.1386 |
| sortino_ratio | -0.7358 |
| max_drawdown | 0.5798 |
| cagr | -0.2867 |
| net_avg_win | 66.1214 |
| net_avg_loss | -83.3247 |
| avg_hold_time_bars | 6.4931 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
