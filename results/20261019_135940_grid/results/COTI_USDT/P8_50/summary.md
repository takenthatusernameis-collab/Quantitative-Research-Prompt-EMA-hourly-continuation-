# EMA Hourly Continuation — COTI/USDT P8_50

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1187 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.9641 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -5.9317 |
| sortino_ratio | -2.8677 |
| max_drawdown | 0.9717 |
| cagr | -0.7495 |
| net_avg_win | 29.8710 |
| net_avg_loss | -41.2280 |
| avg_hold_time_bars | 8.3463 |
| exposure | 0.4503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
