# EMA Hourly Continuation — DAG/USDT P100_200

**Symbol:** DAG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.9862 |
| net_win_rate | 0.5439 |
| gross_profit_factor | 1.1804 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | -0.0148 |
| sortino_ratio | -0.0032 |
| max_drawdown | 0.1269 |
| cagr | -0.0059 |
| net_avg_win | 85.3395 |
| net_avg_loss | -103.1736 |
| avg_hold_time_bars | 13.7193 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
