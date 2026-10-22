# EMA Hourly Continuation — DAG/USDT P8_100

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7768 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9016 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -1.4423 |
| sortino_ratio | -0.4434 |
| max_drawdown | 0.5125 |
| cagr | -0.1858 |
| net_avg_win | 62.3724 |
| net_avg_loss | -75.2777 |
| avg_hold_time_bars | 27.0710 |
| exposure | 0.5722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
