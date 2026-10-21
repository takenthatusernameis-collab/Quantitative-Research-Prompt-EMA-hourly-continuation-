# EMA Hourly Continuation — VELO/USDT P8_200

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 1.0222 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1535 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | 0.1912 |
| sortino_ratio | 0.0523 |
| max_drawdown | 0.1651 |
| cagr | 0.0158 |
| net_avg_win | 95.7767 |
| net_avg_loss | -109.5943 |
| avg_hold_time_bars | 45.4609 |
| exposure | 0.7398 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
