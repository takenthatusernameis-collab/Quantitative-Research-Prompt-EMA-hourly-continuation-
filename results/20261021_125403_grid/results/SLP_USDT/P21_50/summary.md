# EMA Hourly Continuation — SLP/USDT P21_50

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7217 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.9792 |
| sortino_ratio | -1.0048 |
| max_drawdown | 0.7217 |
| cagr | -0.3683 |
| net_avg_win | 66.7233 |
| net_avg_loss | -84.8034 |
| avg_hold_time_bars | 6.7410 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
