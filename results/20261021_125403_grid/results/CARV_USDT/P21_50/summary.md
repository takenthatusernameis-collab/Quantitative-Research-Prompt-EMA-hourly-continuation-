# EMA Hourly Continuation — CARV/USDT P21_50

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.5699 |
| sortino_ratio | -0.8563 |
| max_drawdown | 0.5714 |
| cagr | -0.3238 |
| net_avg_win | 61.0781 |
| net_avg_loss | -83.8298 |
| avg_hold_time_bars | 9.0275 |
| exposure | 0.2220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
