# EMA Hourly Continuation — ANYONE/USDT P21_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8135 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9871 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.1326 |
| sortino_ratio | -0.2881 |
| max_drawdown | 0.3269 |
| cagr | -0.1266 |
| net_avg_win | 80.4084 |
| net_avg_loss | -98.1519 |
| avg_hold_time_bars | 45.2334 |
| exposure | 0.6560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
