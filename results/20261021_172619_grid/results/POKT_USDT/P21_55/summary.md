# EMA Hourly Continuation — POKT/USDT P21_55

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.6385 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -4.0545 |
| sortino_ratio | -1.3583 |
| max_drawdown | 0.8053 |
| cagr | -0.4652 |
| net_avg_win | 57.9360 |
| net_avg_loss | -68.6206 |
| avg_hold_time_bars | 8.0872 |
| exposure | 0.2057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
