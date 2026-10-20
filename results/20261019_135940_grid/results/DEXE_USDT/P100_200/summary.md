# EMA Hourly Continuation — DEXE/USDT P100_200

**Symbol:** DEXE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9109 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.8706 |
| sortino_ratio | -0.4166 |
| max_drawdown | 0.4626 |
| cagr | -0.1788 |
| net_avg_win | 59.1581 |
| net_avg_loss | -85.9471 |
| avg_hold_time_bars | 30.7621 |
| exposure | 0.3468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
