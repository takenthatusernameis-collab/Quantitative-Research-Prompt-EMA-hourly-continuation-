# EMA Hourly Continuation — MOODENG/USDT P20_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7883 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9806 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -1.8652 |
| sortino_ratio | -0.6149 |
| max_drawdown | 0.4948 |
| cagr | -0.2478 |
| net_avg_win | 76.5864 |
| net_avg_loss | -94.9552 |
| avg_hold_time_bars | 8.8650 |
| exposure | 0.2144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
