# EMA Hourly Continuation — CYBER/USDT P55_100

**Symbol:** CYBER/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7823 |
| net_win_rate | 0.5269 |
| gross_profit_factor | 1.0826 |
| gross_win_rate | 0.5269 |
| sharpe_ratio | -1.4551 |
| sortino_ratio | -0.4337 |
| max_drawdown | 0.4517 |
| cagr | -0.1808 |
| net_avg_win | 62.9131 |
| net_avg_loss | -89.5796 |
| avg_hold_time_bars | 7.2717 |
| exposure | 0.1411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
