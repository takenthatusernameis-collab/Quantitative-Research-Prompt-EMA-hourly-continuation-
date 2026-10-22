# EMA Hourly Continuation — AEVO/USDT P8_50

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.7972 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 0.9842 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.9345 |
| sortino_ratio | -0.7453 |
| max_drawdown | 0.6051 |
| cagr | -0.2919 |
| net_avg_win | 62.9695 |
| net_avg_loss | -78.5535 |
| avg_hold_time_bars | 14.7775 |
| exposure | 0.4868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
