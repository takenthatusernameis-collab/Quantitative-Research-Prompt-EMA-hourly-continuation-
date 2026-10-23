# EMA Hourly Continuation — UQC/USDT P34_100

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.2034 |
| net_win_rate | 0.2649 |
| gross_profit_factor | 0.4357 |
| gross_win_rate | 0.2857 |
| sharpe_ratio | -8.0664 |
| sortino_ratio | -2.0963 |
| max_drawdown | 0.9424 |
| cagr | -0.6776 |
| net_avg_win | 27.0412 |
| net_avg_loss | -47.8993 |
| avg_hold_time_bars | 31.8155 |
| exposure | 0.4838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
