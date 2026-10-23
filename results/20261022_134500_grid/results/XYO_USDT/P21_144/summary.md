# EMA Hourly Continuation — XYO/USDT P21_144

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.4583 |
| net_win_rate | 0.4096 |
| gross_profit_factor | 0.7587 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -6.4819 |
| sortino_ratio | -2.2600 |
| max_drawdown | 0.9447 |
| cagr | -0.6771 |
| net_avg_win | 31.1446 |
| net_avg_loss | -47.1424 |
| avg_hold_time_bars | 17.6256 |
| exposure | 0.4985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
