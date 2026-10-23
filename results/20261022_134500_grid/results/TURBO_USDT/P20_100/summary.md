# EMA Hourly Continuation — TURBO/USDT P20_100

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.6620 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -4.0681 |
| sortino_ratio | -1.5132 |
| max_drawdown | 0.7939 |
| cagr | -0.5116 |
| net_avg_win | 56.9776 |
| net_avg_loss | -73.1878 |
| avg_hold_time_bars | 13.1979 |
| exposure | 0.4183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
