# EMA Hourly Continuation — API3/USDT P55_100

**Symbol:** API3/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.5370 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -5.3896 |
| sortino_ratio | -1.9370 |
| max_drawdown | 0.9093 |
| cagr | -0.6078 |
| net_avg_win | 36.0508 |
| net_avg_loss | -54.5747 |
| avg_hold_time_bars | 5.8998 |
| exposure | 0.1740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
