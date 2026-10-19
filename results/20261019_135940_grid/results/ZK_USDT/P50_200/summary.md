# EMA Hourly Continuation — ZK/USDT P50_200

**Symbol:** ZK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.6901 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9150 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.2946 |
| sortino_ratio | -0.6489 |
| max_drawdown | 0.5299 |
| cagr | -0.2635 |
| net_avg_win | 63.9480 |
| net_avg_loss | -84.1600 |
| avg_hold_time_bars | 22.6898 |
| exposure | 0.4137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
