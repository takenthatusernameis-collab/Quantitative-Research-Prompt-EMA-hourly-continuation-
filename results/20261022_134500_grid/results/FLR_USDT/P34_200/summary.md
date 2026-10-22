# EMA Hourly Continuation — FLR/USDT P34_200

**Symbol:** FLR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9326 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.6689 |
| sortino_ratio | -1.2183 |
| max_drawdown | 0.7768 |
| cagr | -0.4481 |
| net_avg_win | 45.2584 |
| net_avg_loss | -68.5510 |
| avg_hold_time_bars | 16.6572 |
| exposure | 0.4263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
