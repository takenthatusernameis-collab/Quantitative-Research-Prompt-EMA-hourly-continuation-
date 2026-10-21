# EMA Hourly Continuation — PUFFER/USDT P21_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 1.1333 |
| net_win_rate | 0.5625 |
| gross_profit_factor | 1.2889 |
| gross_win_rate | 0.5625 |
| sharpe_ratio | 0.7017 |
| sortino_ratio | 0.1771 |
| max_drawdown | 0.0977 |
| cagr | 0.0730 |
| net_avg_win | 96.1772 |
| net_avg_loss | -109.1111 |
| avg_hold_time_bars | 44.9875 |
| exposure | 0.6110 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
