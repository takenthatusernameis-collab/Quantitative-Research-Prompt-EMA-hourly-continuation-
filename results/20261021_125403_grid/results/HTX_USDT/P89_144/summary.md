# EMA Hourly Continuation — HTX/USDT P89_144

**Symbol:** HTX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.3443 |
| net_win_rate | 0.3433 |
| gross_profit_factor | 0.6188 |
| gross_win_rate | 0.3467 |
| sharpe_ratio | -6.3453 |
| sortino_ratio | -1.6056 |
| max_drawdown | 0.8568 |
| cagr | -0.5329 |
| net_avg_win | 43.4992 |
| net_avg_loss | -66.0654 |
| avg_hold_time_bars | 7.8867 |
| exposure | 0.1071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
