# EMA Hourly Continuation — GALA/USDT P20_21

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1219 |
| net_profit_factor | 0.1546 |
| net_win_rate | 0.2830 |
| gross_profit_factor | 0.6109 |
| gross_win_rate | 0.3372 |
| sharpe_ratio | -18.2202 |
| sortino_ratio | -9.6540 |
| max_drawdown | 1.0000 |
| cagr | -0.9957 |
| net_avg_win | 5.3019 |
| net_avg_loss | -13.5345 |
| avg_hold_time_bars | 1.6817 |
| exposure | 0.0932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
