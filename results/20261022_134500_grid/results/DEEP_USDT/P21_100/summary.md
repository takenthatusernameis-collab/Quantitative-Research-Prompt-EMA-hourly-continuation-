# EMA Hourly Continuation — DEEP/USDT P21_100

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7601 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -2.0610 |
| sortino_ratio | -0.6826 |
| max_drawdown | 0.4953 |
| cagr | -0.2768 |
| net_avg_win | 69.0872 |
| net_avg_loss | -90.8946 |
| avg_hold_time_bars | 17.9477 |
| exposure | 0.4471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
