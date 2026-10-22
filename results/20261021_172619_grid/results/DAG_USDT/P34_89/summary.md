# EMA Hourly Continuation — DAG/USDT P34_89

**Symbol:** DAG/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7455 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -1.7388 |
| sortino_ratio | -0.4617 |
| max_drawdown | 0.4345 |
| cagr | -0.1919 |
| net_avg_win | 73.5757 |
| net_avg_loss | -88.9832 |
| avg_hold_time_bars | 10.8621 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
