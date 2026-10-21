# EMA Hourly Continuation — WEMIX/USDT P89_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.5462 |
| net_win_rate | 0.4067 |
| gross_profit_factor | 0.6962 |
| gross_win_rate | 0.4067 |
| sharpe_ratio | -3.6061 |
| sortino_ratio | -0.9215 |
| max_drawdown | 0.6633 |
| cagr | -0.3471 |
| net_avg_win | 59.4765 |
| net_avg_loss | -74.6537 |
| avg_hold_time_bars | 15.0979 |
| exposure | 0.2244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
