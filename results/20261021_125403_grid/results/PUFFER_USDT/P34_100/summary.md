# EMA Hourly Continuation — PUFFER/USDT P34_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.9741 |
| net_win_rate | 0.5444 |
| gross_profit_factor | 1.1834 |
| gross_win_rate | 0.5444 |
| sharpe_ratio | -0.1047 |
| sortino_ratio | -0.0316 |
| max_drawdown | 0.1411 |
| cagr | -0.0222 |
| net_avg_win | 87.6573 |
| net_avg_loss | -107.5285 |
| avg_hold_time_bars | 12.8252 |
| exposure | 0.2533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
