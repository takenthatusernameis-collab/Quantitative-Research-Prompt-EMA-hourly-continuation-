# EMA Hourly Continuation — MOODENG/USDT P26_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7798 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9957 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.9035 |
| sortino_ratio | -0.5910 |
| max_drawdown | 0.4874 |
| cagr | -0.2392 |
| net_avg_win | 79.4909 |
| net_avg_loss | -100.3702 |
| avg_hold_time_bars | 7.2972 |
| exposure | 0.1563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
