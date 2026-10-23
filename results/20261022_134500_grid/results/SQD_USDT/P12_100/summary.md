# EMA Hourly Continuation — SQD/USDT P12_100

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.7338 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.7980 |
| sortino_ratio | -1.0824 |
| max_drawdown | 0.7356 |
| cagr | -0.4031 |
| net_avg_win | 54.4139 |
| net_avg_loss | -73.1388 |
| avg_hold_time_bars | 14.7929 |
| exposure | 0.5069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
