# EMA Hourly Continuation — DOGS/USDT P21_50

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.4257 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.6825 |
| gross_win_rate | 0.4355 |
| sharpe_ratio | -8.3592 |
| sortino_ratio | -3.8767 |
| max_drawdown | 0.9831 |
| cagr | -0.8499 |
| net_avg_win | 18.5393 |
| net_avg_loss | -31.8754 |
| avg_hold_time_bars | 3.8581 |
| exposure | 0.1903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
