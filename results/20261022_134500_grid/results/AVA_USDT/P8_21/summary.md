# EMA Hourly Continuation — AVA/USDT P8_21

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1554 |
| net_profit_factor | 0.3319 |
| net_win_rate | 0.4189 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -12.2591 |
| sortino_ratio | -6.8279 |
| max_drawdown | 0.9998 |
| cagr | -0.9697 |
| net_avg_win | 7.6292 |
| net_avg_loss | -16.5726 |
| avg_hold_time_bars | 3.0187 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
