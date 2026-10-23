# EMA Hourly Continuation — PUNDIX/USDT P21_50

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.4389 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -8.1841 |
| sortino_ratio | -3.6067 |
| max_drawdown | 0.9894 |
| cagr | -0.8348 |
| net_avg_win | 17.9938 |
| net_avg_loss | -31.8782 |
| avg_hold_time_bars | 5.4507 |
| exposure | 0.2435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
