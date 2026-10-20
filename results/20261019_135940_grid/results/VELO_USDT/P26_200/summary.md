# EMA Hourly Continuation — VELO/USDT P26_200

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.7591 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.7276 |
| sortino_ratio | -0.5055 |
| max_drawdown | 0.5465 |
| cagr | -0.2135 |
| net_avg_win | 67.3119 |
| net_avg_loss | -86.6295 |
| avg_hold_time_bars | 28.3193 |
| exposure | 0.5522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
