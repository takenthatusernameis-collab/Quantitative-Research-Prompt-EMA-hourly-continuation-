# EMA Hourly Continuation — OSMO/USDT P12_20

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6844 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 1.0893 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -3.0712 |
| sortino_ratio | -0.8936 |
| max_drawdown | 0.7024 |
| cagr | -0.3347 |
| net_avg_win | 69.1159 |
| net_avg_loss | -98.0592 |
| avg_hold_time_bars | 4.8284 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
