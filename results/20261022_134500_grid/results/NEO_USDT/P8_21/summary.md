# EMA Hourly Continuation — NEO/USDT P8_21

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1674 |
| net_profit_factor | 0.3547 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.8564 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -12.8539 |
| sortino_ratio | -7.4399 |
| max_drawdown | 0.9999 |
| cagr | -0.9778 |
| net_avg_win | 7.6982 |
| net_avg_loss | -16.1415 |
| avg_hold_time_bars | 3.0603 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
