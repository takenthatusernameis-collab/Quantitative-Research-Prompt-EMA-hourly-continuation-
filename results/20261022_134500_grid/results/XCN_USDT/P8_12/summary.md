# EMA Hourly Continuation — XCN/USDT P8_12

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2140 |
| net_profit_factor | 0.1282 |
| net_win_rate | 0.2972 |
| gross_profit_factor | 0.5167 |
| gross_win_rate | 0.3467 |
| sharpe_ratio | -23.0461 |
| sortino_ratio | -15.6688 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 2.3130 |
| net_avg_loss | -7.6270 |
| avg_hold_time_bars | 1.7953 |
| exposure | 0.1746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
