# EMA Hourly Continuation — ZIL/USDT P20_200

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6926 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0529 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -2.1664 |
| sortino_ratio | -0.5950 |
| max_drawdown | 0.5604 |
| cagr | -0.2519 |
| net_avg_win | 60.1082 |
| net_avg_loss | -88.1442 |
| avg_hold_time_bars | 35.8649 |
| exposure | 0.6276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
