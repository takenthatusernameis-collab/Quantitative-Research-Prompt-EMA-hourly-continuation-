# EMA Hourly Continuation — VELO/USDT P20_55

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.5673 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8412 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -5.6933 |
| sortino_ratio | -2.5429 |
| max_drawdown | 0.9573 |
| cagr | -0.7056 |
| net_avg_win | 26.6569 |
| net_avg_loss | -40.4375 |
| avg_hold_time_bars | 5.1834 |
| exposure | 0.2389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
