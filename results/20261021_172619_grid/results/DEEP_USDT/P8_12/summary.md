# EMA Hourly Continuation — DEEP/USDT P8_12

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 1.0199 |
| net_win_rate | 0.5771 |
| gross_profit_factor | 1.3486 |
| gross_win_rate | 0.5771 |
| sharpe_ratio | 0.1507 |
| sortino_ratio | 0.0349 |
| max_drawdown | 0.1684 |
| cagr | 0.0101 |
| net_avg_win | 90.4944 |
| net_avg_loss | -121.0945 |
| avg_hold_time_bars | 5.2488 |
| exposure | 0.0597 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
