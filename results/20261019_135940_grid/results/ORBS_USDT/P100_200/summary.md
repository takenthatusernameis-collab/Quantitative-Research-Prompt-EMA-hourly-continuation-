# EMA Hourly Continuation — ORBS/USDT P100_200

**Symbol:** ORBS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.4395 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.7834 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -5.4490 |
| sortino_ratio | -1.6060 |
| max_drawdown | 0.8588 |
| cagr | -0.5382 |
| net_avg_win | 38.1540 |
| net_avg_loss | -59.4503 |
| avg_hold_time_bars | 10.2217 |
| exposure | 0.2012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
