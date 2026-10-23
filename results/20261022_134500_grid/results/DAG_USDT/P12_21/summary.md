# EMA Hourly Continuation — DAG/USDT P12_21

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1455 |
| net_profit_factor | 0.3100 |
| net_win_rate | 0.3285 |
| gross_profit_factor | 0.6738 |
| gross_win_rate | 0.3608 |
| sharpe_ratio | -16.1788 |
| sortino_ratio | -8.8627 |
| max_drawdown | 1.0000 |
| cagr | -0.9916 |
| net_avg_win | 9.3998 |
| net_avg_loss | -14.8342 |
| avg_hold_time_bars | 2.1691 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
