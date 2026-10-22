# EMA Hourly Continuation — DOGS/USDT P20_100

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.8284 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -1.1435 |
| sortino_ratio | -0.3541 |
| max_drawdown | 0.3061 |
| cagr | -0.1524 |
| net_avg_win | 71.5399 |
| net_avg_loss | -88.1042 |
| avg_hold_time_bars | 18.9850 |
| exposure | 0.4029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
