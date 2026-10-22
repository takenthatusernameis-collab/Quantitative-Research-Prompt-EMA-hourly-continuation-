# EMA Hourly Continuation — JST/USDT P26_55

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.2573 |
| net_win_rate | 0.4137 |
| gross_profit_factor | 0.9339 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -9.4616 |
| sortino_ratio | -3.7764 |
| max_drawdown | 0.9928 |
| cagr | -0.8573 |
| net_avg_win | 10.7143 |
| net_avg_loss | -29.3750 |
| avg_hold_time_bars | 5.3505 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
