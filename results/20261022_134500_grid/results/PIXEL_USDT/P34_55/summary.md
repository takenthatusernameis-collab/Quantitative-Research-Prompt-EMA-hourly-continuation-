# EMA Hourly Continuation — PIXEL/USDT P34_55

**Symbol:** PIXEL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 873 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 1.0402 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -6.2252 |
| sortino_ratio | -2.5993 |
| max_drawdown | 0.9621 |
| cagr | -0.7164 |
| net_avg_win | 29.8328 |
| net_avg_loss | -46.2951 |
| avg_hold_time_bars | 3.6976 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
