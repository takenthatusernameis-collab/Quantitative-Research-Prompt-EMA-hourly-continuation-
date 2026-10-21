# EMA Hourly Continuation — FLR/USDT P100_200

**Symbol:** FLR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7041 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.9257 |
| sortino_ratio | -0.4751 |
| max_drawdown | 0.4380 |
| cagr | -0.1960 |
| net_avg_win | 69.2168 |
| net_avg_loss | -93.7786 |
| avg_hold_time_bars | 11.4714 |
| exposure | 0.1549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
