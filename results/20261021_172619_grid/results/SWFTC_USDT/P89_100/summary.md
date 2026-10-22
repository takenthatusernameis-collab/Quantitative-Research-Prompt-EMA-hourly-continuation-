# EMA Hourly Continuation — SWFTC/USDT P89_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9751 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -1.1688 |
| sortino_ratio | -0.1741 |
| max_drawdown | 0.2375 |
| cagr | -0.0767 |
| net_avg_win | 82.1203 |
| net_avg_loss | -112.1529 |
| avg_hold_time_bars | 6.8056 |
| exposure | 0.0334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
