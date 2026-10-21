# EMA Hourly Continuation — RIO/USDT P8_100

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.8403 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9418 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -1.2691 |
| sortino_ratio | -0.4316 |
| max_drawdown | 0.4389 |
| cagr | -0.1838 |
| net_avg_win | 76.1432 |
| net_avg_loss | -85.6165 |
| avg_hold_time_bars | 22.5089 |
| exposure | 0.5828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
