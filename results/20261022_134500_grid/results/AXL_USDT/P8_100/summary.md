# EMA Hourly Continuation — AXL/USDT P8_100

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 829 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.4294 |
| gross_profit_factor | 0.8068 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -5.8377 |
| sortino_ratio | -2.3543 |
| max_drawdown | 0.9446 |
| cagr | -0.6771 |
| net_avg_win | 33.3733 |
| net_avg_loss | -45.0388 |
| avg_hold_time_bars | 16.8552 |
| exposure | 0.6323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
