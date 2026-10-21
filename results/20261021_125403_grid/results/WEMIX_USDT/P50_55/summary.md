# EMA Hourly Continuation — WEMIX/USDT P50_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 127 |
| net_profit_factor | 0.5959 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -1.9321 |
| sortino_ratio | -0.3110 |
| max_drawdown | 0.3385 |
| cagr | -0.1339 |
| net_avg_win | 78.4047 |
| net_avg_loss | -107.1329 |
| avg_hold_time_bars | 6.8189 |
| exposure | 0.0394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
