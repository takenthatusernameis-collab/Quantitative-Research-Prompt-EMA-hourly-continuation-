# EMA Hourly Continuation — DAG/USDT P55_100

**Symbol:** DAG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.6967 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8622 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -1.8020 |
| sortino_ratio | -0.4047 |
| max_drawdown | 0.3904 |
| cagr | -0.1710 |
| net_avg_win | 74.3924 |
| net_avg_loss | -92.4316 |
| avg_hold_time_bars | 8.5720 |
| exposure | 0.0974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
