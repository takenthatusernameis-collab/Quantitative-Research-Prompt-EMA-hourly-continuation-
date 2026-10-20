# EMA Hourly Continuation — CELR/USDT P100_200

**Symbol:** CELR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.5338 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -3.9783 |
| sortino_ratio | -1.1377 |
| max_drawdown | 0.7456 |
| cagr | -0.4167 |
| net_avg_win | 46.7604 |
| net_avg_loss | -70.2331 |
| avg_hold_time_bars | 9.4597 |
| exposure | 0.1751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
