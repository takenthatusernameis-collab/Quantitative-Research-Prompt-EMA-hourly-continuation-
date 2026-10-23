# EMA Hourly Continuation — GALA/USDT P89_200

**Symbol:** GALA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 1.0194 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.6163 |
| sortino_ratio | -0.7133 |
| max_drawdown | 0.5822 |
| cagr | -0.2886 |
| net_avg_win | 58.7970 |
| net_avg_loss | -85.8329 |
| avg_hold_time_bars | 12.3130 |
| exposure | 0.2110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
