# EMA Hourly Continuation — PROM/USDT P21_34

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.4620 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.7321 |
| gross_win_rate | 0.4169 |
| sharpe_ratio | -4.9873 |
| sortino_ratio | -1.4665 |
| max_drawdown | 0.8318 |
| cagr | -0.5002 |
| net_avg_win | 40.0128 |
| net_avg_loss | -61.3207 |
| avg_hold_time_bars | 4.8056 |
| exposure | 0.0933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
