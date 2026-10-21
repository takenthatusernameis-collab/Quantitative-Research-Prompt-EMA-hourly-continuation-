# EMA Hourly Continuation — VELO/USDT P26_50

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6755 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8509 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.2000 |
| sortino_ratio | -0.6000 |
| max_drawdown | 0.5261 |
| cagr | -0.2398 |
| net_avg_win | 60.2157 |
| net_avg_loss | -78.6338 |
| avg_hold_time_bars | 6.3188 |
| exposure | 0.1054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
