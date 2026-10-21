# EMA Hourly Continuation — PEOPLE/USDT P26_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.8441 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9990 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -0.8727 |
| sortino_ratio | -0.2170 |
| max_drawdown | 0.2929 |
| cagr | -0.0967 |
| net_avg_win | 80.6587 |
| net_avg_loss | -96.1844 |
| avg_hold_time_bars | 41.9802 |
| exposure | 0.5756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
