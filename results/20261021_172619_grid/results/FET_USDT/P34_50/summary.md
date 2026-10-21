# EMA Hourly Continuation — FET/USDT P34_50

**Symbol:** FET/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.6543 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.8518 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -1.7085 |
| sortino_ratio | -0.3240 |
| max_drawdown | 0.3174 |
| cagr | -0.1381 |
| net_avg_win | 71.8937 |
| net_avg_loss | -94.8357 |
| avg_hold_time_bars | 5.8531 |
| exposure | 0.0471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
