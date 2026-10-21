# EMA Hourly Continuation — GRAM/USDT P21_50

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6266 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -3.0294 |
| sortino_ratio | -0.8813 |
| max_drawdown | 0.6444 |
| cagr | -0.3316 |
| net_avg_win | 54.7612 |
| net_avg_loss | -78.1796 |
| avg_hold_time_bars | 7.6053 |
| exposure | 0.1428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
