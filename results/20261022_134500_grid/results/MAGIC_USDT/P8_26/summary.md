# EMA Hourly Continuation — MAGIC/USDT P8_26

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1401 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.9983 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -8.6681 |
| sortino_ratio | -4.5832 |
| max_drawdown | 0.9962 |
| cagr | -0.8901 |
| net_avg_win | 18.9164 |
| net_avg_loss | -28.1932 |
| avg_hold_time_bars | 4.8066 |
| exposure | 0.3061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
