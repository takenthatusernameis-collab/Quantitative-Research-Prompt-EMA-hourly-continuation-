# EMA Hourly Continuation — FLUX/USDT P26_100

**Symbol:** FLUX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9694 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.7498 |
| sortino_ratio | -0.5462 |
| max_drawdown | 0.4934 |
| cagr | -0.2229 |
| net_avg_win | 66.9214 |
| net_avg_loss | -84.7204 |
| avg_hold_time_bars | 13.9937 |
| exposure | 0.3028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
