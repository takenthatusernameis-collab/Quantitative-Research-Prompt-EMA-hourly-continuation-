# EMA Hourly Continuation — AVAX/USDT P8_34

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1383 |
| net_profit_factor | 0.4718 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -9.5583 |
| sortino_ratio | -4.9736 |
| max_drawdown | 0.9982 |
| cagr | -0.9176 |
| net_avg_win | 14.5663 |
| net_avg_loss | -24.5079 |
| avg_hold_time_bars | 5.3507 |
| exposure | 0.3364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
