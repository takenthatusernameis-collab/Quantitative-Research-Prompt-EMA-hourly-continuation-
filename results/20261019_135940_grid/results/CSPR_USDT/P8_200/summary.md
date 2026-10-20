# EMA Hourly Continuation — CSPR/USDT P8_200

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.5523 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.7891 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -5.0381 |
| sortino_ratio | -1.7663 |
| max_drawdown | 0.8821 |
| cagr | -0.5699 |
| net_avg_win | 41.1119 |
| net_avg_loss | -54.7409 |
| avg_hold_time_bars | 26.1348 |
| exposure | 0.7401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
