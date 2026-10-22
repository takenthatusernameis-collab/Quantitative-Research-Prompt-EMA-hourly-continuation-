# EMA Hourly Continuation — RENDER/USDT P89_100

**Symbol:** RENDER/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.4077 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -7.7615 |
| sortino_ratio | -2.7503 |
| max_drawdown | 0.9551 |
| cagr | -0.7609 |
| net_avg_win | 27.9637 |
| net_avg_loss | -54.4549 |
| avg_hold_time_bars | 2.2222 |
| exposure | 0.0623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
