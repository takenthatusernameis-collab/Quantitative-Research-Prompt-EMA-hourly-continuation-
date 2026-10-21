# EMA Hourly Continuation — ANKR/USDT P26_34

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.4200 |
| net_win_rate | 0.3979 |
| gross_profit_factor | 0.6647 |
| gross_win_rate | 0.3979 |
| sharpe_ratio | -4.5462 |
| sortino_ratio | -1.0986 |
| max_drawdown | 0.7216 |
| cagr | -0.3990 |
| net_avg_win | 46.2463 |
| net_avg_loss | -72.7601 |
| avg_hold_time_bars | 8.9331 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
