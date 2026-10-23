# EMA Hourly Continuation — MAGIC/USDT P12_26

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1305 |
| net_profit_factor | 0.4817 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.9643 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -9.0746 |
| sortino_ratio | -4.6357 |
| max_drawdown | 0.9966 |
| cagr | -0.8954 |
| net_avg_win | 16.0824 |
| net_avg_loss | -26.3772 |
| avg_hold_time_bars | 3.7885 |
| exposure | 0.2247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
