# EMA Hourly Continuation — MAGIC/USDT P89_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.5363 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.7981 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -3.5048 |
| sortino_ratio | -0.9424 |
| max_drawdown | 0.6805 |
| cagr | -0.3608 |
| net_avg_win | 48.4988 |
| net_avg_loss | -71.7156 |
| avg_hold_time_bars | 13.4258 |
| exposure | 0.2221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
