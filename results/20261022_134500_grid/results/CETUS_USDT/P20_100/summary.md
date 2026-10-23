# EMA Hourly Continuation — CETUS/USDT P20_100

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0414 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -2.8675 |
| sortino_ratio | -1.0396 |
| max_drawdown | 0.7321 |
| cagr | -0.3905 |
| net_avg_win | 63.1198 |
| net_avg_loss | -82.7139 |
| avg_hold_time_bars | 14.3858 |
| exposure | 0.4303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
