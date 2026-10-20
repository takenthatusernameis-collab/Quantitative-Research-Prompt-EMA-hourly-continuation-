# EMA Hourly Continuation — BRETT/USDT P55_100

**Symbol:** BRETT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.6681 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9936 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -3.5879 |
| sortino_ratio | -1.2763 |
| max_drawdown | 0.7714 |
| cagr | -0.4597 |
| net_avg_win | 52.2275 |
| net_avg_loss | -74.6396 |
| avg_hold_time_bars | 4.9785 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
