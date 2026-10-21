# EMA Hourly Continuation — POKT/USDT P21_26

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.4471 |
| net_win_rate | 0.3495 |
| gross_profit_factor | 0.6287 |
| gross_win_rate | 0.3528 |
| sharpe_ratio | -5.0358 |
| sortino_ratio | -1.2501 |
| max_drawdown | 0.7728 |
| cagr | -0.4425 |
| net_avg_win | 57.7320 |
| net_avg_loss | -69.3778 |
| avg_hold_time_bars | 6.3754 |
| exposure | 0.0891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
