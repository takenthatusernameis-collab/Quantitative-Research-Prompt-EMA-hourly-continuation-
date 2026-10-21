# EMA Hourly Continuation — OP/USDT P144_200

**Symbol:** OP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.7413 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.2289 |
| sortino_ratio | -0.2389 |
| max_drawdown | 0.2573 |
| cagr | -0.1041 |
| net_avg_win | 75.9444 |
| net_avg_loss | -100.2461 |
| avg_hold_time_bars | 9.0000 |
| exposure | 0.0753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
