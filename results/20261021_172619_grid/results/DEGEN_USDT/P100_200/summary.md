# EMA Hourly Continuation — DEGEN/USDT P100_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 1.0167 |
| net_win_rate | 0.5560 |
| gross_profit_factor | 1.2415 |
| gross_win_rate | 0.5560 |
| sharpe_ratio | 0.1297 |
| sortino_ratio | 0.0287 |
| max_drawdown | 0.1459 |
| cagr | 0.0079 |
| net_avg_win | 93.6979 |
| net_avg_loss | -115.4186 |
| avg_hold_time_bars | 16.6293 |
| exposure | 0.1757 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
