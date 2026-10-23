# EMA Hourly Continuation — ALPINE/USDT P50_55

**Symbol:** ALPINE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.2161 |
| net_win_rate | 0.3266 |
| gross_profit_factor | 0.6942 |
| gross_win_rate | 0.4168 |
| sharpe_ratio | -12.0724 |
| sortino_ratio | -4.9555 |
| max_drawdown | 0.9986 |
| cagr | -0.9261 |
| net_avg_win | 10.7140 |
| net_avg_loss | -24.0360 |
| avg_hold_time_bars | 3.3189 |
| exposure | 0.1187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
