# EMA Hourly Continuation — XCH/USDT P34_55

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6024 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8267 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -2.8905 |
| sortino_ratio | -0.7610 |
| max_drawdown | 0.5983 |
| cagr | -0.2957 |
| net_avg_win | 57.5905 |
| net_avg_loss | -78.7281 |
| avg_hold_time_bars | 5.3754 |
| exposure | 0.0833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
