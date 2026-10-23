# EMA Hourly Continuation — MAGIC/USDT P21_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.6689 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 1.0776 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -4.9245 |
| sortino_ratio | -2.0883 |
| max_drawdown | 0.9229 |
| cagr | -0.6307 |
| net_avg_win | 42.5320 |
| net_avg_loss | -59.7514 |
| avg_hold_time_bars | 6.2867 |
| exposure | 0.2572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
