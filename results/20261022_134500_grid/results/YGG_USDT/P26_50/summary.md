# EMA Hourly Continuation — YGG/USDT P26_50

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 980 |
| net_profit_factor | 0.5505 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.9329 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -6.7814 |
| sortino_ratio | -2.9807 |
| max_drawdown | 0.9764 |
| cagr | -0.7665 |
| net_avg_win | 26.5202 |
| net_avg_loss | -40.9039 |
| avg_hold_time_bars | 3.7551 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
