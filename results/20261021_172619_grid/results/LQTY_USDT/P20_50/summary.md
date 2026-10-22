# EMA Hourly Continuation — LQTY/USDT P20_50

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.7480 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 0.9958 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -2.1469 |
| sortino_ratio | -0.7436 |
| max_drawdown | 0.5987 |
| cagr | -0.2890 |
| net_avg_win | 58.2761 |
| net_avg_loss | -78.7077 |
| avg_hold_time_bars | 8.3744 |
| exposure | 0.2217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
