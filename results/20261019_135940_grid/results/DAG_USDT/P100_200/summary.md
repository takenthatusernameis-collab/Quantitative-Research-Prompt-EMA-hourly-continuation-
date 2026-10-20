# EMA Hourly Continuation — DAG/USDT P100_200

**Symbol:** DAG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.5526 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8361 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -3.7112 |
| sortino_ratio | -1.0710 |
| max_drawdown | 0.7420 |
| cagr | -0.4119 |
| net_avg_win | 45.9324 |
| net_avg_loss | -71.2467 |
| avg_hold_time_bars | 8.2075 |
| exposure | 0.1600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
