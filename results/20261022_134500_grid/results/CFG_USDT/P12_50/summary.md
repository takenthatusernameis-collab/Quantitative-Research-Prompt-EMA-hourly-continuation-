# EMA Hourly Continuation — CFG/USDT P12_50

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 870 |
| net_profit_factor | 0.5045 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8375 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -5.1496 |
| sortino_ratio | -2.1327 |
| max_drawdown | 0.9248 |
| cagr | -0.6418 |
| net_avg_win | 23.4098 |
| net_avg_loss | -39.8542 |
| avg_hold_time_bars | 12.6379 |
| exposure | 0.4998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
