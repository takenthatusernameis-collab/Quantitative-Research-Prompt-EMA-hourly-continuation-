# EMA Hourly Continuation — DAG/USDT P34_55

**Symbol:** DAG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.3044 |
| net_win_rate | 0.3823 |
| gross_profit_factor | 0.5643 |
| gross_win_rate | 0.3928 |
| sharpe_ratio | -9.8157 |
| sortino_ratio | -4.0561 |
| max_drawdown | 0.9952 |
| cagr | -0.8795 |
| net_avg_win | 13.2766 |
| net_avg_loss | -26.9916 |
| avg_hold_time_bars | 2.7249 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
