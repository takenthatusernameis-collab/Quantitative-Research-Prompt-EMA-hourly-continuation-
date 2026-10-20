# EMA Hourly Continuation — XCH/USDT P34_50

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.2827 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.8579 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -11.1906 |
| sortino_ratio | -5.3298 |
| max_drawdown | 0.9989 |
| cagr | -0.9331 |
| net_avg_win | 8.9249 |
| net_avg_loss | -20.5379 |
| avg_hold_time_bars | 2.4861 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
