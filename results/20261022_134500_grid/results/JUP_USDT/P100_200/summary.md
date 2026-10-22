# EMA Hourly Continuation — JUP/USDT P100_200

**Symbol:** JUP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8668 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -3.2956 |
| sortino_ratio | -0.9061 |
| max_drawdown | 0.6813 |
| cagr | -0.3550 |
| net_avg_win | 51.3008 |
| net_avg_loss | -76.9834 |
| avg_hold_time_bars | 8.8909 |
| exposure | 0.1556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
