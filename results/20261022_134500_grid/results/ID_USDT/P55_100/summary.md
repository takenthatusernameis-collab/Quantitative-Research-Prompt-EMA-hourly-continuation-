# EMA Hourly Continuation — ID/USDT P55_100

**Symbol:** ID/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.4931 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8247 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -4.3205 |
| sortino_ratio | -1.4882 |
| max_drawdown | 0.8248 |
| cagr | -0.4970 |
| net_avg_win | 29.4503 |
| net_avg_loss | -51.8972 |
| avg_hold_time_bars | 6.0051 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
