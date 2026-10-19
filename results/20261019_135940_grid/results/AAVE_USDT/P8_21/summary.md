# EMA Hourly Continuation — AAVE/USDT P8_21

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1662 |
| net_profit_factor | 0.3491 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.7939 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -12.5207 |
| sortino_ratio | -7.1754 |
| max_drawdown | 0.9999 |
| cagr | -0.9754 |
| net_avg_win | 7.6180 |
| net_avg_loss | -16.0357 |
| avg_hold_time_bars | 3.1498 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
