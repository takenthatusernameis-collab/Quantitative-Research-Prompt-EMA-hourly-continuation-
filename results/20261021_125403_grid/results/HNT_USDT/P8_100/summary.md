# EMA Hourly Continuation — HNT/USDT P8_100

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.8152 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -1.3903 |
| sortino_ratio | -0.4547 |
| max_drawdown | 0.4481 |
| cagr | -0.1914 |
| net_avg_win | 70.1447 |
| net_avg_loss | -84.7418 |
| avg_hold_time_bars | 25.1947 |
| exposure | 0.6001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
