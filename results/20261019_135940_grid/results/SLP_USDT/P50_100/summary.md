# EMA Hourly Continuation — SLP/USDT P50_100

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.5367 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8919 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -6.1468 |
| sortino_ratio | -2.3398 |
| max_drawdown | 0.9439 |
| cagr | -0.6797 |
| net_avg_win | 34.3339 |
| net_avg_loss | -49.8651 |
| avg_hold_time_bars | 5.9656 |
| exposure | 0.1969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
