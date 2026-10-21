# EMA Hourly Continuation — TRAC/USDT P8_200

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7348 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8664 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -1.9037 |
| sortino_ratio | -0.4976 |
| max_drawdown | 0.4621 |
| cagr | -0.2050 |
| net_avg_win | 77.2882 |
| net_avg_loss | -89.7501 |
| avg_hold_time_bars | 47.7771 |
| exposure | 0.7405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
