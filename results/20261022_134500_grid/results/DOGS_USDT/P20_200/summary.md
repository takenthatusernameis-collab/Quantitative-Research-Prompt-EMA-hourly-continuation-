# EMA Hourly Continuation — DOGS/USDT P20_200

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6728 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.7936 |
| sortino_ratio | -0.8359 |
| max_drawdown | 0.6117 |
| cagr | -0.3313 |
| net_avg_win | 63.6860 |
| net_avg_loss | -87.6353 |
| avg_hold_time_bars | 29.5450 |
| exposure | 0.6097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
