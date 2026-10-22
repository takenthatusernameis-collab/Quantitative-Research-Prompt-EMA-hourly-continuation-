# EMA Hourly Continuation — IOTX/USDT P50_89

**Symbol:** IOTX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6403 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8811 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.6979 |
| sortino_ratio | -0.7385 |
| max_drawdown | 0.5715 |
| cagr | -0.2864 |
| net_avg_win | 59.1427 |
| net_avg_loss | -81.4767 |
| avg_hold_time_bars | 6.9973 |
| exposure | 0.1167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
