# EMA Hourly Continuation — XCN/USDT P8_55

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1323 |
| net_profit_factor | 0.3611 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.6307 |
| gross_win_rate | 0.4263 |
| sharpe_ratio | -9.7770 |
| sortino_ratio | -4.9549 |
| max_drawdown | 0.9982 |
| cagr | -0.9198 |
| net_avg_win | 10.2771 |
| net_avg_loss | -20.1865 |
| avg_hold_time_bars | 7.6364 |
| exposure | 0.4592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
