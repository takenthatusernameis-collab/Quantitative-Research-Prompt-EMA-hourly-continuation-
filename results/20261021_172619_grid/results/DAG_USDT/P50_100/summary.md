# EMA Hourly Continuation — DAG/USDT P50_100

**Symbol:** DAG/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7515 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9199 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -1.5145 |
| sortino_ratio | -0.3643 |
| max_drawdown | 0.3770 |
| cagr | -0.1554 |
| net_avg_win | 76.2910 |
| net_avg_loss | -93.9708 |
| avg_hold_time_bars | 9.0702 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
