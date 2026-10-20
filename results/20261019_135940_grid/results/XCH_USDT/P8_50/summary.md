# EMA Hourly Continuation — XCH/USDT P8_50

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1326 |
| net_profit_factor | 0.4888 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -8.0488 |
| sortino_ratio | -4.1060 |
| max_drawdown | 0.9938 |
| cagr | -0.8660 |
| net_avg_win | 16.3547 |
| net_avg_loss | -26.0911 |
| avg_hold_time_bars | 7.7202 |
| exposure | 0.4653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
