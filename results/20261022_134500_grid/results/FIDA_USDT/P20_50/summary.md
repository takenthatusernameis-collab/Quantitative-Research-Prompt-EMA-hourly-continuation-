# EMA Hourly Continuation — FIDA/USDT P20_50

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.4931 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.8672 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -7.0658 |
| sortino_ratio | -3.0827 |
| max_drawdown | 0.9780 |
| cagr | -0.7743 |
| net_avg_win | 22.6730 |
| net_avg_loss | -35.7441 |
| avg_hold_time_bars | 5.8674 |
| exposure | 0.2544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
