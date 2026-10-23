# EMA Hourly Continuation — METIS/USDT P21_55

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.4812 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8359 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -7.2244 |
| sortino_ratio | -3.1576 |
| max_drawdown | 0.9810 |
| cagr | -0.7869 |
| net_avg_win | 21.4731 |
| net_avg_loss | -34.9576 |
| avg_hold_time_bars | 5.1495 |
| exposure | 0.2254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
