# EMA Hourly Continuation — POLYX/USDT P34_100

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0429 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -3.2534 |
| sortino_ratio | -1.1238 |
| max_drawdown | 0.7544 |
| cagr | -0.4124 |
| net_avg_win | 50.3650 |
| net_avg_loss | -73.3562 |
| avg_hold_time_bars | 11.0435 |
| exposure | 0.3002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
