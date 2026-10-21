# EMA Hourly Continuation — TAIKO/USDT P8_20

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.8117 |
| net_win_rate | 0.5410 |
| gross_profit_factor | 1.1620 |
| gross_win_rate | 0.5410 |
| sharpe_ratio | -1.5802 |
| sortino_ratio | -0.5503 |
| max_drawdown | 0.5198 |
| cagr | -0.2239 |
| net_avg_win | 65.6476 |
| net_avg_loss | -95.3242 |
| avg_hold_time_bars | 6.1148 |
| exposure | 0.1613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
