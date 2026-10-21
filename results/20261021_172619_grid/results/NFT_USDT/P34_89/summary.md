# EMA Hourly Continuation — NFT/USDT P34_89

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.3695 |
| net_win_rate | 0.3382 |
| gross_profit_factor | 0.6625 |
| gross_win_rate | 0.3406 |
| sharpe_ratio | -7.4913 |
| sortino_ratio | -2.2120 |
| max_drawdown | 0.9334 |
| cagr | -0.6508 |
| net_avg_win | 39.1553 |
| net_avg_loss | -54.1571 |
| avg_hold_time_bars | 14.4501 |
| exposure | 0.2700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
