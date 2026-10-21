# EMA Hourly Continuation — SLP/USDT P50_100

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7224 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9662 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.1899 |
| sortino_ratio | -0.6593 |
| max_drawdown | 0.5457 |
| cagr | -0.2617 |
| net_avg_win | 63.9351 |
| net_avg_loss | -85.3594 |
| avg_hold_time_bars | 8.3982 |
| exposure | 0.1687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
