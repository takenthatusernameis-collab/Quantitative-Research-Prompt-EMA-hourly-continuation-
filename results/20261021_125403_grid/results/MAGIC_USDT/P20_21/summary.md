# EMA Hourly Continuation — MAGIC/USDT P20_21

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8995 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.0101 |
| sortino_ratio | -0.6982 |
| max_drawdown | 0.6247 |
| cagr | -0.2765 |
| net_avg_win | 67.9578 |
| net_avg_loss | -96.6119 |
| avg_hold_time_bars | 5.2290 |
| exposure | 0.0623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
