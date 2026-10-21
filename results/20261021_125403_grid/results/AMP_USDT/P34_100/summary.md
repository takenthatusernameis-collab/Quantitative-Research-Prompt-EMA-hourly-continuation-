# EMA Hourly Continuation — AMP/USDT P34_100

**Symbol:** AMP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.5405 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.7213 |
| gross_win_rate | 0.4141 |
| sharpe_ratio | -4.4256 |
| sortino_ratio | -1.3953 |
| max_drawdown | 0.8124 |
| cagr | -0.4747 |
| net_avg_win | 45.9945 |
| net_avg_loss | -60.1496 |
| avg_hold_time_bars | 12.4626 |
| exposure | 0.2804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
