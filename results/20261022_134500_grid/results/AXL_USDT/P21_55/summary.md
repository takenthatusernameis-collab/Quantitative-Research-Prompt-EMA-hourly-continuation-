# EMA Hourly Continuation — AXL/USDT P21_55

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.5488 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -7.3860 |
| sortino_ratio | -3.3051 |
| max_drawdown | 0.9823 |
| cagr | -0.7958 |
| net_avg_win | 27.8344 |
| net_avg_loss | -37.2589 |
| avg_hold_time_bars | 5.1441 |
| exposure | 0.2358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
