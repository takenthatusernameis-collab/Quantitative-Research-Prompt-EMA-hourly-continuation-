# EMA Hourly Continuation — ASTR/USDT P55_100

**Symbol:** ASTR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6459 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -2.5852 |
| sortino_ratio | -0.7178 |
| max_drawdown | 0.5831 |
| cagr | -0.2811 |
| net_avg_win | 56.3254 |
| net_avg_loss | -81.8353 |
| avg_hold_time_bars | 9.1667 |
| exposure | 0.1568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
