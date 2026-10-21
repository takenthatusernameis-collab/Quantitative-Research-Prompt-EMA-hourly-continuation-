# EMA Hourly Continuation — ORBS/USDT P21_200

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7540 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -1.7948 |
| sortino_ratio | -0.4779 |
| max_drawdown | 0.4764 |
| cagr | -0.1974 |
| net_avg_win | 76.9473 |
| net_avg_loss | -95.2904 |
| avg_hold_time_bars | 39.8229 |
| exposure | 0.6335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
