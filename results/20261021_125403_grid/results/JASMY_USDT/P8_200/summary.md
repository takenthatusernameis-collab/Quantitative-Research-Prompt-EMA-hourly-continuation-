# EMA Hourly Continuation — JASMY/USDT P8_200

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 1.0999 |
| net_win_rate | 0.5657 |
| gross_profit_factor | 1.2892 |
| gross_win_rate | 0.5657 |
| sharpe_ratio | 0.5698 |
| sortino_ratio | 0.1379 |
| max_drawdown | 0.1346 |
| cagr | 0.0553 |
| net_avg_win | 102.8138 |
| net_avg_loss | -121.7545 |
| avg_hold_time_bars | 64.0219 |
| exposure | 0.7974 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
