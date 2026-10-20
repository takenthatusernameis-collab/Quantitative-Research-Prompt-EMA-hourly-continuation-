# EMA Hourly Continuation — MOVR/USDT P8_34

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1425 |
| net_profit_factor | 0.4653 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -8.0506 |
| sortino_ratio | -4.2549 |
| max_drawdown | 0.9949 |
| cagr | -0.8763 |
| net_avg_win | 13.5030 |
| net_avg_loss | -23.7281 |
| avg_hold_time_bars | 5.5179 |
| exposure | 0.3574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
