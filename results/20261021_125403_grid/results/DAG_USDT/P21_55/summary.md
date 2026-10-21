# EMA Hourly Continuation — DAG/USDT P21_55

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8321 |
| net_win_rate | 0.5137 |
| gross_profit_factor | 1.0436 |
| gross_win_rate | 0.5137 |
| sharpe_ratio | -1.1531 |
| sortino_ratio | -0.3316 |
| max_drawdown | 0.4053 |
| cagr | -0.1432 |
| net_avg_win | 77.3449 |
| net_avg_loss | -98.2006 |
| avg_hold_time_bars | 8.0848 |
| exposure | 0.1474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
