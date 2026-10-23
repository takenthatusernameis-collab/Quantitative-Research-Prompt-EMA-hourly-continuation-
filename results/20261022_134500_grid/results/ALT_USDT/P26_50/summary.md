# EMA Hourly Continuation — ALT/USDT P26_50

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 837 |
| net_profit_factor | 0.5043 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8586 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -6.4705 |
| sortino_ratio | -2.6382 |
| max_drawdown | 0.9607 |
| cagr | -0.7202 |
| net_avg_win | 26.3075 |
| net_avg_loss | -41.5280 |
| avg_hold_time_bars | 5.1135 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
