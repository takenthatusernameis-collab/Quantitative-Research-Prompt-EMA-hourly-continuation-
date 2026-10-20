# EMA Hourly Continuation — BRETT/USDT P50_55

**Symbol:** BRETT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.2739 |
| net_win_rate | 0.3727 |
| gross_profit_factor | 0.6355 |
| gross_win_rate | 0.4008 |
| sharpe_ratio | -10.4069 |
| sortino_ratio | -4.1975 |
| max_drawdown | 0.9947 |
| cagr | -0.8900 |
| net_avg_win | 13.4951 |
| net_avg_loss | -29.2701 |
| avg_hold_time_bars | 1.8619 |
| exposure | 0.0668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
