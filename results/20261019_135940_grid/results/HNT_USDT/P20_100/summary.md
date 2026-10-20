# EMA Hourly Continuation — HNT/USDT P20_100

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.5477 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.7778 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -4.8333 |
| sortino_ratio | -1.8241 |
| max_drawdown | 0.8954 |
| cagr | -0.5818 |
| net_avg_win | 33.6065 |
| net_avg_loss | -49.2091 |
| avg_hold_time_bars | 12.7385 |
| exposure | 0.4163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
