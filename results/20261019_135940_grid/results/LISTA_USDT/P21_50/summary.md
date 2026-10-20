# EMA Hourly Continuation — LISTA/USDT P21_50

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 850 |
| net_profit_factor | 0.5406 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8343 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -6.2079 |
| sortino_ratio | -2.6547 |
| max_drawdown | 0.9468 |
| cagr | -0.7153 |
| net_avg_win | 29.7034 |
| net_avg_loss | -43.3818 |
| avg_hold_time_bars | 5.6047 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
