# EMA Hourly Continuation — BOSON/USDT P8_50

**Symbol:** BOSON/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -6.1913 |
| sortino_ratio | -2.7958 |
| max_drawdown | 0.9659 |
| cagr | -0.7394 |
| net_avg_win | 29.5481 |
| net_avg_loss | -39.3412 |
| avg_hold_time_bars | 9.1303 |
| exposure | 0.4333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
