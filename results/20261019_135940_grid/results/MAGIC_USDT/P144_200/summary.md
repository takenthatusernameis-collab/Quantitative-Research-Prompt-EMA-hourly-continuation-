# EMA Hourly Continuation — MAGIC/USDT P144_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5153 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8695 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -4.3054 |
| sortino_ratio | -1.1962 |
| max_drawdown | 0.7769 |
| cagr | -0.4418 |
| net_avg_win | 46.9594 |
| net_avg_loss | -74.4498 |
| avg_hold_time_bars | 5.4677 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
