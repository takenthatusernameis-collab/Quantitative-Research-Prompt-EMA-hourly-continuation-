# EMA Hourly Continuation — MAGIC/USDT P21_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7918 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9604 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.3144 |
| sortino_ratio | -0.3187 |
| max_drawdown | 0.4149 |
| cagr | -0.1377 |
| net_avg_win | 83.7958 |
| net_avg_loss | -100.8179 |
| avg_hold_time_bars | 50.8339 |
| exposure | 0.6678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
