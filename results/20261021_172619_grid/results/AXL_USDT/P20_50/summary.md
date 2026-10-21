# EMA Hourly Continuation — AXL/USDT P20_50

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.6198 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.8024 |
| gross_win_rate | 0.4314 |
| sharpe_ratio | -4.2279 |
| sortino_ratio | -1.4615 |
| max_drawdown | 0.8303 |
| cagr | -0.4910 |
| net_avg_win | 51.6882 |
| net_avg_loss | -63.2807 |
| avg_hold_time_bars | 6.9615 |
| exposure | 0.1884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
