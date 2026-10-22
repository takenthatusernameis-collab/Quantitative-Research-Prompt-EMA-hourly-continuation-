# EMA Hourly Continuation — YGG/USDT P50_144

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.8468 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0369 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -1.0222 |
| sortino_ratio | -0.2861 |
| max_drawdown | 0.3453 |
| cagr | -0.1253 |
| net_avg_win | 81.2497 |
| net_avg_loss | -100.0537 |
| avg_hold_time_bars | 15.8979 |
| exposure | 0.2748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
