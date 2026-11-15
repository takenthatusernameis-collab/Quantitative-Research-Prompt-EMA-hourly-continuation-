# EMA Hourly Continuation — CERE/USDT P20_100

**Symbol:** CERE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.4984 |
| net_win_rate | 0.3840 |
| gross_profit_factor | 0.8353 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -8.4395 |
| sortino_ratio | -3.2781 |
| max_drawdown | 0.9864 |
| cagr | -0.8138 |
| net_avg_win | 33.4129 |
| net_avg_loss | -41.7940 |
| avg_hold_time_bars | 12.4771 |
| exposure | 0.4327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
