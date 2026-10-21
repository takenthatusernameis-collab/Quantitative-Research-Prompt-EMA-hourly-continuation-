# EMA Hourly Continuation — UMA/USDT P26_55

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -2.7753 |
| sortino_ratio | -0.9087 |
| max_drawdown | 0.6575 |
| cagr | -0.3412 |
| net_avg_win | 57.1549 |
| net_avg_loss | -80.9765 |
| avg_hold_time_bars | 7.7510 |
| exposure | 0.1839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
