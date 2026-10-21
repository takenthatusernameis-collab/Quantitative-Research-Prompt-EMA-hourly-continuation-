# EMA Hourly Continuation — GALA/USDT P34_50

**Symbol:** GALA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.5923 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8056 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -2.7206 |
| sortino_ratio | -0.6274 |
| max_drawdown | 0.5370 |
| cagr | -0.2500 |
| net_avg_win | 64.4512 |
| net_avg_loss | -86.4488 |
| avg_hold_time_bars | 5.0267 |
| exposure | 0.0599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
