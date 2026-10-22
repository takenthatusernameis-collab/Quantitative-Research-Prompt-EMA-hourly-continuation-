# EMA Hourly Continuation — ZIL/USDT P55_100

**Symbol:** ZIL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7753 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0834 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -1.4360 |
| sortino_ratio | -0.3885 |
| max_drawdown | 0.3987 |
| cagr | -0.1630 |
| net_avg_win | 67.5697 |
| net_avg_loss | -95.4503 |
| avg_hold_time_bars | 8.1449 |
| exposure | 0.1303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
