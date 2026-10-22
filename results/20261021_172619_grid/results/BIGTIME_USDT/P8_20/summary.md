# EMA Hourly Continuation — BIGTIME/USDT P8_20

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.5950 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8138 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -4.4817 |
| sortino_ratio | -1.5912 |
| max_drawdown | 0.8424 |
| cagr | -0.5192 |
| net_avg_win | 44.8328 |
| net_avg_loss | -59.7618 |
| avg_hold_time_bars | 6.0913 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
