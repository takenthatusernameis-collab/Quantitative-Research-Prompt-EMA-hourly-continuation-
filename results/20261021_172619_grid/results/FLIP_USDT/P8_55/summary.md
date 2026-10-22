# EMA Hourly Continuation — FLIP/USDT P8_55

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -2.9459 |
| sortino_ratio | -0.9585 |
| max_drawdown | 0.6758 |
| cagr | -0.3584 |
| net_avg_win | 58.7407 |
| net_avg_loss | -78.8362 |
| avg_hold_time_bars | 22.4019 |
| exposure | 0.5346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
