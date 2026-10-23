# EMA Hourly Continuation — ARKM/USDT P8_34

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1420 |
| net_profit_factor | 0.5366 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.8324 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -8.5240 |
| sortino_ratio | -4.5183 |
| max_drawdown | 0.9960 |
| cagr | -0.8878 |
| net_avg_win | 18.7549 |
| net_avg_loss | -26.6995 |
| avg_hold_time_bars | 5.3669 |
| exposure | 0.3464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
