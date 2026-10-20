# EMA Hourly Continuation — ASTR/USDT P34_89

**Symbol:** ASTR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.6097 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0439 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -3.7056 |
| sortino_ratio | -1.2771 |
| max_drawdown | 0.7946 |
| cagr | -0.4601 |
| net_avg_win | 40.6630 |
| net_avg_loss | -67.1369 |
| avg_hold_time_bars | 9.8692 |
| exposure | 0.2698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
