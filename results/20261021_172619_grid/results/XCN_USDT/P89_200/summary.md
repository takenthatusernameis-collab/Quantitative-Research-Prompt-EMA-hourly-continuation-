# EMA Hourly Continuation — XCN/USDT P89_200

**Symbol:** XCN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.6705 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -2.2627 |
| sortino_ratio | -0.5411 |
| max_drawdown | 0.5019 |
| cagr | -0.2213 |
| net_avg_win | 74.1554 |
| net_avg_loss | -90.7472 |
| avg_hold_time_bars | 16.8486 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
