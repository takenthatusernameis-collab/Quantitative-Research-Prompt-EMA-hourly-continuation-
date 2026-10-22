# EMA Hourly Continuation — G/USDT P12_21

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6256 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9966 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -3.6857 |
| sortino_ratio | -1.2885 |
| max_drawdown | 0.7234 |
| cagr | -0.4442 |
| net_avg_win | 47.7873 |
| net_avg_loss | -74.8968 |
| avg_hold_time_bars | 5.3399 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
