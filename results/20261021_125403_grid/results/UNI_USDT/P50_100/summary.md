# EMA Hourly Continuation — UNI/USDT P50_100

**Symbol:** UNI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8516 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1138 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -0.7800 |
| sortino_ratio | -0.2003 |
| max_drawdown | 0.2573 |
| cagr | -0.0897 |
| net_avg_win | 71.8032 |
| net_avg_loss | -95.7051 |
| avg_hold_time_bars | 10.5918 |
| exposure | 0.1521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
