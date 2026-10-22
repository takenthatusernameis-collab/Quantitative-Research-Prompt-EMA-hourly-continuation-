# EMA Hourly Continuation — EGLD/USDT P26_34

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.2153 |
| net_win_rate | 0.3786 |
| gross_profit_factor | 0.7220 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -13.0527 |
| sortino_ratio | -6.2712 |
| max_drawdown | 0.9997 |
| cagr | -0.9625 |
| net_avg_win | 6.6108 |
| net_avg_loss | -18.7091 |
| avg_hold_time_bars | 2.2026 |
| exposure | 0.1097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
