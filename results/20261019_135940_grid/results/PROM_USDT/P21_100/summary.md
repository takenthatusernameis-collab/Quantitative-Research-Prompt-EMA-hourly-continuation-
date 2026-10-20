# EMA Hourly Continuation — PROM/USDT P21_100

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.4795 |
| net_win_rate | 0.4183 |
| gross_profit_factor | 0.8221 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -6.3448 |
| sortino_ratio | -2.3305 |
| max_drawdown | 0.9475 |
| cagr | -0.6857 |
| net_avg_win | 29.8250 |
| net_avg_loss | -44.7348 |
| avg_hold_time_bars | 12.8309 |
| exposure | 0.4071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
