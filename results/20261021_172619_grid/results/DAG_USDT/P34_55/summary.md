# EMA Hourly Continuation — DAG/USDT P34_55

**Symbol:** DAG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.7320 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -1.3977 |
| sortino_ratio | -0.2869 |
| max_drawdown | 0.3008 |
| cagr | -0.1235 |
| net_avg_win | 76.2048 |
| net_avg_loss | -100.1358 |
| avg_hold_time_bars | 6.1748 |
| exposure | 0.0578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
