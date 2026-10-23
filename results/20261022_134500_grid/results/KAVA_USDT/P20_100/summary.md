# EMA Hourly Continuation — KAVA/USDT P20_100

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5400 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -5.6601 |
| sortino_ratio | -2.0456 |
| max_drawdown | 0.9264 |
| cagr | -0.6355 |
| net_avg_win | 36.5069 |
| net_avg_loss | -53.7980 |
| avg_hold_time_bars | 15.8189 |
| exposure | 0.4803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
