# EMA Hourly Continuation — EIGEN/USDT P8_12

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.3362 |
| net_win_rate | 0.3935 |
| gross_profit_factor | 0.7028 |
| gross_win_rate | 0.4178 |
| sharpe_ratio | -15.0075 |
| sortino_ratio | -9.0775 |
| max_drawdown | 0.9999 |
| cagr | -0.9911 |
| net_avg_win | 8.7004 |
| net_avg_loss | -16.7927 |
| avg_hold_time_bars | 1.6951 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
