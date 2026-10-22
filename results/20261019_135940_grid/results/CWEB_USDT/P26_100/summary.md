# EMA Hourly Continuation — CWEB/USDT P26_100

**Symbol:** CWEB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.5089 |
| net_win_rate | 0.4160 |
| gross_profit_factor | 0.8385 |
| gross_win_rate | 0.4216 |
| sharpe_ratio | -6.0537 |
| sortino_ratio | -1.9596 |
| max_drawdown | 0.9199 |
| cagr | -0.6284 |
| net_avg_win | 42.6027 |
| net_avg_loss | -59.6425 |
| avg_hold_time_bars | 16.1810 |
| exposure | 0.3942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
