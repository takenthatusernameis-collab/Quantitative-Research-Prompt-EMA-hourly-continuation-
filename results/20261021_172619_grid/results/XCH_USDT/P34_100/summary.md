# EMA Hourly Continuation — XCH/USDT P34_100

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7445 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9442 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -1.8717 |
| sortino_ratio | -0.5788 |
| max_drawdown | 0.4927 |
| cagr | -0.2341 |
| net_avg_win | 62.1104 |
| net_avg_loss | -79.9397 |
| avg_hold_time_bars | 13.8483 |
| exposure | 0.2946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
