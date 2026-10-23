# EMA Hourly Continuation — TURBO/USDT P20_55

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.6359 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9656 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -5.4556 |
| sortino_ratio | -2.3895 |
| max_drawdown | 0.9134 |
| cagr | -0.6823 |
| net_avg_win | 41.5648 |
| net_avg_loss | -58.7533 |
| avg_hold_time_bars | 5.5341 |
| exposure | 0.2436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
