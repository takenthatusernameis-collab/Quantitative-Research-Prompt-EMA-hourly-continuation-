# EMA Hourly Continuation — FLOKI/USDT P20_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.6365 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -4.1316 |
| sortino_ratio | -1.5644 |
| max_drawdown | 0.8569 |
| cagr | -0.5254 |
| net_avg_win | 43.0747 |
| net_avg_loss | -61.4215 |
| avg_hold_time_bars | 12.8368 |
| exposure | 0.4219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
