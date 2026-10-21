# EMA Hourly Continuation — ZBCN/USDT P8_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 1.0667 |
| net_win_rate | 0.5519 |
| gross_profit_factor | 1.2097 |
| gross_win_rate | 0.5519 |
| sharpe_ratio | 0.5174 |
| sortino_ratio | 0.1562 |
| max_drawdown | 0.1701 |
| cagr | 0.0609 |
| net_avg_win | 107.2119 |
| net_avg_loss | -123.7789 |
| avg_hold_time_bars | 36.8467 |
| exposure | 0.7228 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
