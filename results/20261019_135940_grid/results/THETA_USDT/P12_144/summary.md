# EMA Hourly Continuation — THETA/USDT P12_144

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.7070 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -2.4158 |
| sortino_ratio | -0.7338 |
| max_drawdown | 0.6108 |
| cagr | -0.2936 |
| net_avg_win | 61.3461 |
| net_avg_loss | -84.5545 |
| avg_hold_time_bars | 32.9375 |
| exposure | 0.6947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
