# EMA Hourly Continuation — ADA/USDT P26_200

**Symbol:** ADA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 1.0069 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -2.5609 |
| sortino_ratio | -0.6802 |
| max_drawdown | 0.5994 |
| cagr | -0.2852 |
| net_avg_win | 56.1473 |
| net_avg_loss | -86.1953 |
| avg_hold_time_bars | 34.3836 |
| exposure | 0.5705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
