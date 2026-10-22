# EMA Hourly Continuation — ALGO/USDT P21_100

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6277 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -3.9286 |
| sortino_ratio | -1.4232 |
| max_drawdown | 0.8327 |
| cagr | -0.5009 |
| net_avg_win | 42.9554 |
| net_avg_loss | -63.7102 |
| avg_hold_time_bars | 12.5149 |
| exposure | 0.3823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
