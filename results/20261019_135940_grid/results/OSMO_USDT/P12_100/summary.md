# EMA Hourly Continuation — OSMO/USDT P12_100

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.6883 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 1.0509 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -3.5379 |
| sortino_ratio | -1.2908 |
| max_drawdown | 0.7958 |
| cagr | -0.4575 |
| net_avg_win | 53.3120 |
| net_avg_loss | -73.3921 |
| avg_hold_time_bars | 18.9760 |
| exposure | 0.5762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
