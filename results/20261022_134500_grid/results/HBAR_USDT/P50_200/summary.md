# EMA Hourly Continuation — HBAR/USDT P50_200

**Symbol:** HBAR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7055 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0362 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -2.0312 |
| sortino_ratio | -0.5395 |
| max_drawdown | 0.4873 |
| cagr | -0.2269 |
| net_avg_win | 62.9874 |
| net_avg_loss | -92.3481 |
| avg_hold_time_bars | 23.2360 |
| exposure | 0.3760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
