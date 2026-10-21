# EMA Hourly Continuation — VELO/USDT P8_50

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.8083 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 0.9695 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -1.6135 |
| sortino_ratio | -0.6096 |
| max_drawdown | 0.5688 |
| cagr | -0.2468 |
| net_avg_win | 61.7025 |
| net_avg_loss | -76.1170 |
| avg_hold_time_bars | 11.8407 |
| exposure | 0.3751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
