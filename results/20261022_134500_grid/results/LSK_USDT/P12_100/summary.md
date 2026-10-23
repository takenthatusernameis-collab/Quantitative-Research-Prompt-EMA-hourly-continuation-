# EMA Hourly Continuation — LSK/USDT P12_100

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6296 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.8290 |
| sortino_ratio | -1.3160 |
| max_drawdown | 0.8072 |
| cagr | -0.4692 |
| net_avg_win | 48.8568 |
| net_avg_loss | -66.5496 |
| avg_hold_time_bars | 21.0033 |
| exposure | 0.5728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
