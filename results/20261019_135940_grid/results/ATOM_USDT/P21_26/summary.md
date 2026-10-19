# EMA Hourly Continuation — ATOM/USDT P21_26

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.1465 |
| net_win_rate | 0.3289 |
| gross_profit_factor | 0.5977 |
| gross_win_rate | 0.3932 |
| sharpe_ratio | -15.5067 |
| sortino_ratio | -7.7100 |
| max_drawdown | 1.0000 |
| cagr | -0.9850 |
| net_avg_win | 4.6654 |
| net_avg_loss | -15.6014 |
| avg_hold_time_bars | 1.8499 |
| exposure | 0.0941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
