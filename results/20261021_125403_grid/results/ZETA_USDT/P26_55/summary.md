# EMA Hourly Continuation — ZETA/USDT P26_55

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -2.2826 |
| sortino_ratio | -0.7201 |
| max_drawdown | 0.5728 |
| cagr | -0.2803 |
| net_avg_win | 62.5275 |
| net_avg_loss | -84.5179 |
| avg_hold_time_bars | 7.3292 |
| exposure | 0.1612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
