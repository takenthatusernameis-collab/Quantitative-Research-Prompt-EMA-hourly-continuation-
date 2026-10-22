# EMA Hourly Continuation — SLP/USDT P8_100

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.7520 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9178 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.1987 |
| sortino_ratio | -0.7220 |
| max_drawdown | 0.5905 |
| cagr | -0.2834 |
| net_avg_win | 67.9632 |
| net_avg_loss | -81.9499 |
| avg_hold_time_bars | 26.9023 |
| exposure | 0.6505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
