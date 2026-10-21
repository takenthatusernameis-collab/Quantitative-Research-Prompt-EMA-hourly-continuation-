# EMA Hourly Continuation — JASMY/USDT P100_144

**Symbol:** JASMY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 1.1204 |
| net_win_rate | 0.5990 |
| gross_profit_factor | 1.4792 |
| gross_win_rate | 0.5990 |
| sharpe_ratio | 0.5607 |
| sortino_ratio | 0.1192 |
| max_drawdown | 0.0759 |
| cagr | 0.0474 |
| net_avg_win | 92.6503 |
| net_avg_loss | -123.5431 |
| avg_hold_time_bars | 8.0918 |
| exposure | 0.0761 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
