# EMA Hourly Continuation — RSR/USDT P21_200

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.7441 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -2.0089 |
| sortino_ratio | -0.5702 |
| max_drawdown | 0.5101 |
| cagr | -0.2378 |
| net_avg_win | 73.3347 |
| net_avg_loss | -92.8709 |
| avg_hold_time_bars | 33.1881 |
| exposure | 0.6095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
