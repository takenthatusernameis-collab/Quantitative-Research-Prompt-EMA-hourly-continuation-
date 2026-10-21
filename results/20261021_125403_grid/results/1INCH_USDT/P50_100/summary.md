# EMA Hourly Continuation — 1INCH/USDT P50_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6542 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9056 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -2.7964 |
| sortino_ratio | -0.7960 |
| max_drawdown | 0.6076 |
| cagr | -0.3055 |
| net_avg_win | 60.6652 |
| net_avg_loss | -82.9707 |
| avg_hold_time_bars | 8.8990 |
| exposure | 0.1602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
