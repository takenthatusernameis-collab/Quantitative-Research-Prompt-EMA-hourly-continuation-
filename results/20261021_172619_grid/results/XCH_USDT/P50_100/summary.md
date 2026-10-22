# EMA Hourly Continuation — XCH/USDT P50_100

**Symbol:** XCH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -1.9893 |
| sortino_ratio | -0.5471 |
| max_drawdown | 0.4712 |
| cagr | -0.2221 |
| net_avg_win | 62.8865 |
| net_avg_loss | -83.4312 |
| avg_hold_time_bars | 10.1378 |
| exposure | 0.1705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
