# EMA Hourly Continuation — BONK/USDT P21_200

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 1.0194 |
| net_win_rate | 0.5415 |
| gross_profit_factor | 1.1754 |
| gross_win_rate | 0.5451 |
| sharpe_ratio | 0.1556 |
| sortino_ratio | 0.0375 |
| max_drawdown | 0.1951 |
| cagr | 0.0109 |
| net_avg_win | 96.5764 |
| net_avg_loss | -111.8981 |
| avg_hold_time_bars | 49.6715 |
| exposure | 0.6254 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
