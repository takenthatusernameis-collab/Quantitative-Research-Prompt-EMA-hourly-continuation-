# EMA Hourly Continuation — DODO/USDT P20_100

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.5848 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -5.3980 |
| sortino_ratio | -2.0351 |
| max_drawdown | 0.9181 |
| cagr | -0.6213 |
| net_avg_win | 40.7288 |
| net_avg_loss | -54.0713 |
| avg_hold_time_bars | 13.5878 |
| exposure | 0.4445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
