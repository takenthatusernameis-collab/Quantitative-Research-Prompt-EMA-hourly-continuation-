# EMA Hourly Continuation — BAND/USDT P26_200

**Symbol:** BAND/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8201 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.0982 |
| sortino_ratio | -0.2946 |
| max_drawdown | 0.3608 |
| cagr | -0.1284 |
| net_avg_win | 74.5636 |
| net_avg_loss | -93.5382 |
| avg_hold_time_bars | 32.6799 |
| exposure | 0.5220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
