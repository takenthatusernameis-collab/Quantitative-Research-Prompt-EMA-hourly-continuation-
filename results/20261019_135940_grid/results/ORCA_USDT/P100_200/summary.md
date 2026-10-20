# EMA Hourly Continuation — ORCA/USDT P100_200

**Symbol:** ORCA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.4596 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.7654 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -4.6464 |
| sortino_ratio | -1.3269 |
| max_drawdown | 0.8142 |
| cagr | -0.4756 |
| net_avg_win | 38.9973 |
| net_avg_loss | -62.9152 |
| avg_hold_time_bars | 8.5693 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
