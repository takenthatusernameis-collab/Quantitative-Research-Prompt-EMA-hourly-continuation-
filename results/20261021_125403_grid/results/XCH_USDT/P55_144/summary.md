# EMA Hourly Continuation — XCH/USDT P55_144

**Symbol:** XCH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7713 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9688 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -1.4917 |
| sortino_ratio | -0.3987 |
| max_drawdown | 0.3695 |
| cagr | -0.1678 |
| net_avg_win | 72.4388 |
| net_avg_loss | -91.2665 |
| avg_hold_time_bars | 14.7708 |
| exposure | 0.2343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
