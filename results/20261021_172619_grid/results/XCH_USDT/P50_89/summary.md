# EMA Hourly Continuation — XCH/USDT P50_89

**Symbol:** XCH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7310 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9726 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.6499 |
| sortino_ratio | -0.4358 |
| max_drawdown | 0.4300 |
| cagr | -0.1813 |
| net_avg_win | 63.4786 |
| net_avg_loss | -86.3330 |
| avg_hold_time_bars | 8.8407 |
| exposure | 0.1362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
