# EMA Hourly Continuation — CATI/USDT P8_26

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.6900 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -2.7645 |
| sortino_ratio | -0.9339 |
| max_drawdown | 0.5929 |
| cagr | -0.3499 |
| net_avg_win | 59.6408 |
| net_avg_loss | -78.2857 |
| avg_hold_time_bars | 7.9398 |
| exposure | 0.2024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
