# EMA Hourly Continuation — CPOOL/USDT P34_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7603 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9112 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.7524 |
| sortino_ratio | -0.5166 |
| max_drawdown | 0.5020 |
| cagr | -0.2129 |
| net_avg_win | 69.5779 |
| net_avg_loss | -84.9144 |
| avg_hold_time_bars | 9.8972 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
