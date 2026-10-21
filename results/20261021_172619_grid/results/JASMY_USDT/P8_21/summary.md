# EMA Hourly Continuation — JASMY/USDT P8_21

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6936 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.4450 |
| sortino_ratio | -0.7239 |
| max_drawdown | 0.5827 |
| cagr | -0.2827 |
| net_avg_win | 62.8032 |
| net_avg_loss | -81.7293 |
| avg_hold_time_bars | 5.8395 |
| exposure | 0.1141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
