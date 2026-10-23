# EMA Hourly Continuation — STRAX/USDT P12_50

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1052 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.9119 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -7.4577 |
| sortino_ratio | -3.3965 |
| max_drawdown | 0.9849 |
| cagr | -0.8128 |
| net_avg_win | 27.9956 |
| net_avg_loss | -38.8392 |
| avg_hold_time_bars | 8.2709 |
| exposure | 0.3978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
