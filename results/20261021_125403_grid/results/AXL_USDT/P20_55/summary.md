# EMA Hourly Continuation — AXL/USDT P20_55

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7947 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -4.2488 |
| sortino_ratio | -1.4726 |
| max_drawdown | 0.8313 |
| cagr | -0.4946 |
| net_avg_win | 52.1246 |
| net_avg_loss | -62.9665 |
| avg_hold_time_bars | 7.9103 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
