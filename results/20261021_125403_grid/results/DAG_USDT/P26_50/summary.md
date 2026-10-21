# EMA Hourly Continuation — DAG/USDT P26_50

**Symbol:** DAG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.7681 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9793 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.3433 |
| sortino_ratio | -0.3154 |
| max_drawdown | 0.3292 |
| cagr | -0.1355 |
| net_avg_win | 75.6885 |
| net_avg_loss | -97.8100 |
| avg_hold_time_bars | 6.7100 |
| exposure | 0.0820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
