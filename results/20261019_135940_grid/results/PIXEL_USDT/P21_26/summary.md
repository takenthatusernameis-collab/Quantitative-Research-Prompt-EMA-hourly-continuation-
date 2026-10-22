# EMA Hourly Continuation — PIXEL/USDT P21_26

**Symbol:** PIXEL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1176 |
| net_profit_factor | 0.3321 |
| net_win_rate | 0.3767 |
| gross_profit_factor | 0.8330 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -12.6063 |
| sortino_ratio | -6.2016 |
| max_drawdown | 0.9997 |
| cagr | -0.9590 |
| net_avg_win | 11.2206 |
| net_avg_loss | -20.4196 |
| avg_hold_time_bars | 2.5043 |
| exposure | 0.1333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
