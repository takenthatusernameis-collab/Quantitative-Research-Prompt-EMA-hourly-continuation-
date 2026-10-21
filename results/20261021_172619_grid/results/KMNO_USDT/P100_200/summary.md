# EMA Hourly Continuation — KMNO/USDT P100_200

**Symbol:** KMNO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7276 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9304 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -1.6405 |
| sortino_ratio | -0.3807 |
| max_drawdown | 0.3781 |
| cagr | -0.1622 |
| net_avg_win | 74.5411 |
| net_avg_loss | -96.3779 |
| avg_hold_time_bars | 13.3244 |
| exposure | 0.1612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
