# EMA Hourly Continuation — STRK/USDT P20_50

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -6.2854 |
| sortino_ratio | -2.8042 |
| max_drawdown | 0.9663 |
| cagr | -0.7377 |
| net_avg_win | 25.2342 |
| net_avg_loss | -39.5980 |
| avg_hold_time_bars | 4.6089 |
| exposure | 0.2078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
