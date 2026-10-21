# EMA Hourly Continuation — LSK/USDT P8_20

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 1.0978 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -3.8806 |
| sortino_ratio | -1.4916 |
| max_drawdown | 0.8503 |
| cagr | -0.4958 |
| net_avg_win | 53.0284 |
| net_avg_loss | -74.5334 |
| avg_hold_time_bars | 6.2304 |
| exposure | 0.2028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
