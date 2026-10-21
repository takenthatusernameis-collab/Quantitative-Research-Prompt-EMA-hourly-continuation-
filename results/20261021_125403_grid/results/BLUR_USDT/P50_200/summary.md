# EMA Hourly Continuation — BLUR/USDT P50_200

**Symbol:** BLUR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 1.0491 |
| net_win_rate | 0.5581 |
| gross_profit_factor | 1.2443 |
| gross_win_rate | 0.5581 |
| sharpe_ratio | 0.2953 |
| sortino_ratio | 0.0699 |
| max_drawdown | 0.1437 |
| cagr | 0.0254 |
| net_avg_win | 93.8848 |
| net_avg_loss | -113.0065 |
| avg_hold_time_bars | 36.4232 |
| exposure | 0.4401 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
