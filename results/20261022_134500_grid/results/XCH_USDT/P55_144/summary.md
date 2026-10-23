# EMA Hourly Continuation — XCH/USDT P55_144

**Symbol:** XCH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.5007 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -4.8669 |
| sortino_ratio | -1.6341 |
| max_drawdown | 0.8666 |
| cagr | -0.5516 |
| net_avg_win | 33.9485 |
| net_avg_loss | -54.7538 |
| avg_hold_time_bars | 9.7033 |
| exposure | 0.2527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
