# EMA Hourly Continuation — XCH/USDT P26_89

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.7201 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -2.0729 |
| sortino_ratio | -0.6654 |
| max_drawdown | 0.5599 |
| cagr | -0.2638 |
| net_avg_win | 56.3383 |
| net_avg_loss | -73.7251 |
| avg_hold_time_bars | 13.5644 |
| exposure | 0.3114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
