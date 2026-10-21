# EMA Hourly Continuation — SAFE/USDT P21_100

**Symbol:** SAFE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.8478 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0380 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.0932 |
| sortino_ratio | -0.3331 |
| max_drawdown | 0.4026 |
| cagr | -0.1447 |
| net_avg_win | 78.4448 |
| net_avg_loss | -96.7575 |
| avg_hold_time_bars | 19.6004 |
| exposure | 0.4021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
