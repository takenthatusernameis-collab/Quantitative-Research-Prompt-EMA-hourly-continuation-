# EMA Hourly Continuation — HBAR/USDT P21_100

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.8807 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1209 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -0.7905 |
| sortino_ratio | -0.2445 |
| max_drawdown | 0.2984 |
| cagr | -0.1094 |
| net_avg_win | 76.3376 |
| net_avg_loss | -98.3752 |
| avg_hold_time_bars | 18.3660 |
| exposure | 0.3832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
