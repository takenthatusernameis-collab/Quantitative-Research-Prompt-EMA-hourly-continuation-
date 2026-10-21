# EMA Hourly Continuation — CGPT/USDT P21_50

**Symbol:** CGPT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6902 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8895 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -2.5656 |
| sortino_ratio | -0.7950 |
| max_drawdown | 0.6163 |
| cagr | -0.3051 |
| net_avg_win | 59.8494 |
| net_avg_loss | -77.6604 |
| avg_hold_time_bars | 7.5508 |
| exposure | 0.1620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
