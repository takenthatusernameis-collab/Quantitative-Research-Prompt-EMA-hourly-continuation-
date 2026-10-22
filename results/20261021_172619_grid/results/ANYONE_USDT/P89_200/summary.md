# EMA Hourly Continuation — ANYONE/USDT P89_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.7004 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.8137 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -1.6972 |
| sortino_ratio | -0.3919 |
| max_drawdown | 0.4069 |
| cagr | -0.1657 |
| net_avg_win | 72.0396 |
| net_avg_loss | -86.2374 |
| avg_hold_time_bars | 17.5188 |
| exposure | 0.2116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
