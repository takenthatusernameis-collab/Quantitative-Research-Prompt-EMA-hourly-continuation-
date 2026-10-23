# EMA Hourly Continuation — ASTR/USDT P8_26

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1390 |
| net_profit_factor | 0.4280 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8906 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -9.3891 |
| sortino_ratio | -4.9235 |
| max_drawdown | 0.9979 |
| cagr | -0.9123 |
| net_avg_win | 11.9293 |
| net_avg_loss | -22.8353 |
| avg_hold_time_bars | 4.6604 |
| exposure | 0.2931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
