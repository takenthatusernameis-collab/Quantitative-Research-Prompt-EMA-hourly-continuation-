# EMA Hourly Continuation — LUNC/USDT P20_34

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1236 |
| net_profit_factor | 0.2381 |
| net_win_rate | 0.3617 |
| gross_profit_factor | 0.6764 |
| gross_win_rate | 0.4005 |
| sharpe_ratio | -13.7689 |
| sortino_ratio | -6.9700 |
| max_drawdown | 0.9999 |
| cagr | -0.9724 |
| net_avg_win | 6.9910 |
| net_avg_loss | -16.6334 |
| avg_hold_time_bars | 2.4296 |
| exposure | 0.1365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
