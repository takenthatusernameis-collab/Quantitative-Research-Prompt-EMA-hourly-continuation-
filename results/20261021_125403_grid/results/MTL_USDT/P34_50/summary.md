# EMA Hourly Continuation — MTL/USDT P34_50

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.8424 |
| gross_win_rate | 0.4369 |
| sharpe_ratio | -4.7276 |
| sortino_ratio | -1.3747 |
| max_drawdown | 0.8105 |
| cagr | -0.4728 |
| net_avg_win | 47.6488 |
| net_avg_loss | -71.4984 |
| avg_hold_time_bars | 7.9175 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
