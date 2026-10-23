# EMA Hourly Continuation — DAG/USDT P8_50

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.4503 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.7004 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -8.8185 |
| sortino_ratio | -4.2449 |
| max_drawdown | 0.9955 |
| cagr | -0.8834 |
| net_avg_win | 16.3426 |
| net_avg_loss | -25.7605 |
| avg_hold_time_bars | 7.8378 |
| exposure | 0.4282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
