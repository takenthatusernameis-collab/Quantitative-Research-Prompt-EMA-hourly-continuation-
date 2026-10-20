# EMA Hourly Continuation — ANYONE/USDT P34_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6465 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8385 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -2.8864 |
| sortino_ratio | -0.8715 |
| max_drawdown | 0.6223 |
| cagr | -0.3350 |
| net_avg_win | 58.5778 |
| net_avg_loss | -76.3825 |
| avg_hold_time_bars | 18.9100 |
| exposure | 0.3927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
