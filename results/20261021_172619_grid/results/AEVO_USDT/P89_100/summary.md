# EMA Hourly Continuation — AEVO/USDT P89_100

**Symbol:** AEVO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.5792 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8338 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -2.1791 |
| sortino_ratio | -0.3967 |
| max_drawdown | 0.3785 |
| cagr | -0.1662 |
| net_avg_win | 68.3998 |
| net_avg_loss | -98.1925 |
| avg_hold_time_bars | 5.1043 |
| exposure | 0.0376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
