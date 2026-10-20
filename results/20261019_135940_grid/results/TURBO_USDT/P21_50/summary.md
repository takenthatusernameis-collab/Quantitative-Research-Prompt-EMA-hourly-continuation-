# EMA Hourly Continuation — TURBO/USDT P21_50

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 847 |
| net_profit_factor | 0.6225 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -6.0840 |
| sortino_ratio | -2.7353 |
| max_drawdown | 0.9390 |
| cagr | -0.7309 |
| net_avg_win | 39.1608 |
| net_avg_loss | -54.7194 |
| avg_hold_time_bars | 4.3802 |
| exposure | 0.2024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
