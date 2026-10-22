# EMA Hourly Continuation — PENDLE/USDT P20_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.6749 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -3.0672 |
| sortino_ratio | -1.1697 |
| max_drawdown | 0.7523 |
| cagr | -0.4223 |
| net_avg_win | 43.0034 |
| net_avg_loss | -63.0215 |
| avg_hold_time_bars | 12.0248 |
| exposure | 0.3968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
