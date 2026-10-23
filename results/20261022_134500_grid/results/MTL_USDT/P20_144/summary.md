# EMA Hourly Continuation — MTL/USDT P20_144

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.5986 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.9245 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -3.6093 |
| sortino_ratio | -1.0847 |
| max_drawdown | 0.7453 |
| cagr | -0.4083 |
| net_avg_win | 51.6253 |
| net_avg_loss | -73.4239 |
| avg_hold_time_bars | 27.2646 |
| exposure | 0.5688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
