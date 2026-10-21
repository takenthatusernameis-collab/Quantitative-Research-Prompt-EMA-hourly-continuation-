# EMA Hourly Continuation — UNI/USDT P55_100

**Symbol:** UNI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.8181 |
| net_win_rate | 0.5240 |
| gross_profit_factor | 1.0782 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -0.9842 |
| sortino_ratio | -0.2511 |
| max_drawdown | 0.3045 |
| cagr | -0.1099 |
| net_avg_win | 69.5567 |
| net_avg_loss | -93.5776 |
| avg_hold_time_bars | 8.5463 |
| exposure | 0.1216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
