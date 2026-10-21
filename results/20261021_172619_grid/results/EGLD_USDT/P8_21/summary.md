# EMA Hourly Continuation — EGLD/USDT P8_21

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6879 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.9324 |
| sortino_ratio | -1.0461 |
| max_drawdown | 0.7026 |
| cagr | -0.3795 |
| net_avg_win | 50.4597 |
| net_avg_loss | -71.7099 |
| avg_hold_time_bars | 5.3549 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
