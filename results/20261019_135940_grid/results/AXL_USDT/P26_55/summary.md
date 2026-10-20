# EMA Hourly Continuation — AXL/USDT P26_55

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.5448 |
| net_win_rate | 0.4196 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -7.7764 |
| sortino_ratio | -3.4120 |
| max_drawdown | 0.9848 |
| cagr | -0.8088 |
| net_avg_win | 28.9494 |
| net_avg_loss | -38.4163 |
| avg_hold_time_bars | 4.4629 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
