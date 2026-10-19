# EMA Hourly Continuation — LUNC/USDT P26_100

**Symbol:** LUNC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.4903 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -5.6712 |
| sortino_ratio | -2.1737 |
| max_drawdown | 0.9310 |
| cagr | -0.6475 |
| net_avg_win | 26.4647 |
| net_avg_loss | -45.8173 |
| avg_hold_time_bars | 9.4441 |
| exposure | 0.3151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
