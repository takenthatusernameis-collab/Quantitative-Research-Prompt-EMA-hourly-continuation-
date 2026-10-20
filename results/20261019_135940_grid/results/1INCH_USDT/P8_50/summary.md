# EMA Hourly Continuation — 1INCH/USDT P8_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.5052 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -7.4804 |
| sortino_ratio | -3.4756 |
| max_drawdown | 0.9867 |
| cagr | -0.8189 |
| net_avg_win | 20.6803 |
| net_avg_loss | -32.6792 |
| avg_hold_time_bars | 9.6727 |
| exposure | 0.4823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
