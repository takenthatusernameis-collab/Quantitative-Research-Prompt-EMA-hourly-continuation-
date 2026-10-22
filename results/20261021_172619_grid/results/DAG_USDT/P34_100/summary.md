# EMA Hourly Continuation — DAG/USDT P34_100

**Symbol:** DAG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7568 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9010 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -1.6157 |
| sortino_ratio | -0.4297 |
| max_drawdown | 0.4016 |
| cagr | -0.1801 |
| net_avg_win | 73.5907 |
| net_avg_loss | -88.2117 |
| avg_hold_time_bars | 13.8281 |
| exposure | 0.2194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
