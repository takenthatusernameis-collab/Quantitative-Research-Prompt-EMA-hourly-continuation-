# EMA Hourly Continuation — ATOM/USDT P55_144

**Symbol:** ATOM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.8285 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.0881 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.9292 |
| sortino_ratio | -0.2401 |
| max_drawdown | 0.2902 |
| cagr | -0.1059 |
| net_avg_win | 70.0726 |
| net_avg_loss | -94.0378 |
| avg_hold_time_bars | 14.7882 |
| exposure | 0.2158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
