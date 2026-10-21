# EMA Hourly Continuation — XMR/USDT P100_144

**Symbol:** XMR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.5087 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.7263 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -2.9523 |
| sortino_ratio | -0.6024 |
| max_drawdown | 0.5067 |
| cagr | -0.2413 |
| net_avg_win | 60.2133 |
| net_avg_loss | -85.5453 |
| avg_hold_time_bars | 5.6927 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
