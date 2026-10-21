# EMA Hourly Continuation — ZIL/USDT P55_200

**Symbol:** ZIL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0248 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.0660 |
| sortino_ratio | -0.2581 |
| max_drawdown | 0.2758 |
| cagr | -0.1133 |
| net_avg_win | 76.5495 |
| net_avg_loss | -97.9010 |
| avg_hold_time_bars | 27.8211 |
| exposure | 0.3604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
