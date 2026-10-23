# EMA Hourly Continuation — DAG/USDT P20_100

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.5145 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.7788 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -5.8427 |
| sortino_ratio | -2.2227 |
| max_drawdown | 0.9427 |
| cagr | -0.6744 |
| net_avg_win | 30.4691 |
| net_avg_loss | -45.0375 |
| avg_hold_time_bars | 10.7609 |
| exposure | 0.3703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
