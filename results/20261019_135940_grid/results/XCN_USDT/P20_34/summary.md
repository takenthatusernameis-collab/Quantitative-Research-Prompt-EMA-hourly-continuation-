# EMA Hourly Continuation — XCN/USDT P20_34

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1372 |
| net_profit_factor | 0.2397 |
| net_win_rate | 0.3579 |
| gross_profit_factor | 0.5967 |
| gross_win_rate | 0.3878 |
| sharpe_ratio | -14.6557 |
| sortino_ratio | -7.7609 |
| max_drawdown | 1.0000 |
| cagr | -0.9838 |
| net_avg_win | 6.4208 |
| net_avg_loss | -14.9288 |
| avg_hold_time_bars | 2.6735 |
| exposure | 0.1667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
