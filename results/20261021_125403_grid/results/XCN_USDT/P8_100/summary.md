# EMA Hourly Continuation — XCN/USDT P8_100

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7828 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9627 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -1.8296 |
| sortino_ratio | -0.6120 |
| max_drawdown | 0.5226 |
| cagr | -0.2476 |
| net_avg_win | 68.1343 |
| net_avg_loss | -84.2342 |
| avg_hold_time_bars | 22.6138 |
| exposure | 0.5643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
