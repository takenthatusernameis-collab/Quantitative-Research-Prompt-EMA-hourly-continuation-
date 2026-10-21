# EMA Hourly Continuation — POKT/USDT P20_50

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6508 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4408 |
| sharpe_ratio | -3.7835 |
| sortino_ratio | -1.2539 |
| max_drawdown | 0.7818 |
| cagr | -0.4396 |
| net_avg_win | 59.3876 |
| net_avg_loss | -71.4017 |
| avg_hold_time_bars | 7.9071 |
| exposure | 0.1964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
