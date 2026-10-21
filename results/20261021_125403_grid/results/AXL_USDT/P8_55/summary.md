# EMA Hourly Continuation — AXL/USDT P8_55

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 735 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8993 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -3.1908 |
| sortino_ratio | -1.2252 |
| max_drawdown | 0.7787 |
| cagr | -0.4328 |
| net_avg_win | 58.5608 |
| net_avg_loss | -69.9936 |
| avg_hold_time_bars | 14.4939 |
| exposure | 0.4821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
