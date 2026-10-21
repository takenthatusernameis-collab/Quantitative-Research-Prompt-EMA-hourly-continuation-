# EMA Hourly Continuation — ANYONE/USDT P34_55

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.5358 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.6790 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -3.4528 |
| sortino_ratio | -0.8955 |
| max_drawdown | 0.6174 |
| cagr | -0.3420 |
| net_avg_win | 56.0244 |
| net_avg_loss | -73.6023 |
| avg_hold_time_bars | 5.7672 |
| exposure | 0.0889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
