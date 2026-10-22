# EMA Hourly Continuation — UMA/USDT P34_55

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6089 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -3.4364 |
| sortino_ratio | -0.9993 |
| max_drawdown | 0.6974 |
| cagr | -0.3702 |
| net_avg_win | 55.1126 |
| net_avg_loss | -80.1825 |
| avg_hold_time_bars | 6.4600 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
