# EMA Hourly Continuation — DGB/USDT P21_34

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5923 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8239 |
| gross_win_rate | 0.4397 |
| sharpe_ratio | -2.8184 |
| sortino_ratio | -0.6441 |
| max_drawdown | 0.5473 |
| cagr | -0.2566 |
| net_avg_win | 67.5216 |
| net_avg_loss | -89.4506 |
| avg_hold_time_bars | 6.5097 |
| exposure | 0.0760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
