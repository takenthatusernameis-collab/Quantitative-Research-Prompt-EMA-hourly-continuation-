# EMA Hourly Continuation — TRX/USDT P26_100

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.5058 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 1.0089 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -4.3454 |
| sortino_ratio | -1.2413 |
| max_drawdown | 0.7663 |
| cagr | -0.4337 |
| net_avg_win | 41.1714 |
| net_avg_loss | -76.9167 |
| avg_hold_time_bars | 16.6452 |
| exposure | 0.2943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
