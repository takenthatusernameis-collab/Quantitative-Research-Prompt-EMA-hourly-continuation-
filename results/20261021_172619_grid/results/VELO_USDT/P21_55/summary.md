# EMA Hourly Continuation — VELO/USDT P21_55

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.7271 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -1.9509 |
| sortino_ratio | -0.6358 |
| max_drawdown | 0.5729 |
| cagr | -0.2533 |
| net_avg_win | 54.5170 |
| net_avg_loss | -71.3300 |
| avg_hold_time_bars | 7.7505 |
| exposure | 0.1835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
