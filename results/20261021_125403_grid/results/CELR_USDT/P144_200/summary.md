# EMA Hourly Continuation — CELR/USDT P144_200

**Symbol:** CELR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5242 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.7246 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -2.9838 |
| sortino_ratio | -0.6795 |
| max_drawdown | 0.5564 |
| cagr | -0.2687 |
| net_avg_win | 54.1719 |
| net_avg_loss | -78.5749 |
| avg_hold_time_bars | 6.7938 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
