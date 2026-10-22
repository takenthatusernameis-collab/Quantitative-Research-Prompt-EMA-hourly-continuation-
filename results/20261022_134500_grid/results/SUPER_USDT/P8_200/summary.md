# EMA Hourly Continuation — SUPER/USDT P8_200

**Symbol:** SUPER/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 1.0377 |
| net_win_rate | 0.5733 |
| gross_profit_factor | 1.3393 |
| gross_win_rate | 0.5765 |
| sharpe_ratio | 0.2611 |
| sortino_ratio | 0.0657 |
| max_drawdown | 0.1633 |
| cagr | 0.0232 |
| net_avg_win | 92.5470 |
| net_avg_loss | -119.8161 |
| avg_hold_time_bars | 59.9674 |
| exposure | 0.8368 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
