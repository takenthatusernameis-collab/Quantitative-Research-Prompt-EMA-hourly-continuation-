# EMA Hourly Continuation — BCH/USDT P26_100

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6944 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.4954 |
| sortino_ratio | -0.7382 |
| max_drawdown | 0.6021 |
| cagr | -0.2867 |
| net_avg_win | 63.0901 |
| net_avg_loss | -84.3031 |
| avg_hold_time_bars | 17.1916 |
| exposure | 0.3345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
