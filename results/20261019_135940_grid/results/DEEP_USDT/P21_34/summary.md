# EMA Hourly Continuation — DEEP/USDT P21_34

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 831 |
| net_profit_factor | 0.5133 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.8458 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -8.1106 |
| sortino_ratio | -3.6527 |
| max_drawdown | 0.9764 |
| cagr | -0.8418 |
| net_avg_win | 28.5006 |
| net_avg_loss | -42.6507 |
| avg_hold_time_bars | 2.6462 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
