# EMA Hourly Continuation — XCH/USDT P50_55

**Symbol:** XCH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 124 |
| net_profit_factor | 0.4858 |
| net_win_rate | 0.4113 |
| gross_profit_factor | 0.6970 |
| gross_win_rate | 0.4113 |
| sharpe_ratio | -2.4045 |
| sortino_ratio | -0.3812 |
| max_drawdown | 0.3777 |
| cagr | -0.1613 |
| net_avg_win | 66.1224 |
| net_avg_loss | -95.0982 |
| avg_hold_time_bars | 5.6694 |
| exposure | 0.0320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
