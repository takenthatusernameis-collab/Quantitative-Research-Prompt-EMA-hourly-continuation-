# EMA Hourly Continuation — THETA/USDT P8_12

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 1.0412 |
| net_win_rate | 0.5918 |
| gross_profit_factor | 1.4352 |
| gross_win_rate | 0.5918 |
| sharpe_ratio | 0.2524 |
| sortino_ratio | 0.0582 |
| max_drawdown | 0.1579 |
| cagr | 0.0201 |
| net_avg_win | 89.4262 |
| net_avg_loss | -124.5315 |
| avg_hold_time_bars | 4.3429 |
| exposure | 0.0484 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
