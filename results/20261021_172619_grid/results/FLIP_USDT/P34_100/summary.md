# EMA Hourly Continuation — FLIP/USDT P34_100

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9430 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.4685 |
| sortino_ratio | -0.6214 |
| max_drawdown | 0.5384 |
| cagr | -0.2515 |
| net_avg_win | 63.8000 |
| net_avg_loss | -89.5576 |
| avg_hold_time_bars | 19.1289 |
| exposure | 0.2765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
