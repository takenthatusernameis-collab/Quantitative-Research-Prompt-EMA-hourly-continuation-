# EMA Hourly Continuation — UQC/USDT P34_50

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.1028 |
| net_win_rate | 0.2406 |
| gross_profit_factor | 0.2840 |
| gross_win_rate | 0.2581 |
| sharpe_ratio | -9.8558 |
| sortino_ratio | -2.8569 |
| max_drawdown | 0.9811 |
| cagr | -0.7928 |
| net_avg_win | 11.7140 |
| net_avg_loss | -36.0916 |
| avg_hold_time_bars | 25.8772 |
| exposure | 0.4673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
