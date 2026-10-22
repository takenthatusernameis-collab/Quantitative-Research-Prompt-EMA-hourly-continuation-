# EMA Hourly Continuation — UNI/USDT P20_50

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.4446 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8294 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -7.8776 |
| sortino_ratio | -3.5383 |
| max_drawdown | 0.9884 |
| cagr | -0.8289 |
| net_avg_win | 17.3848 |
| net_avg_loss | -31.1583 |
| avg_hold_time_bars | 4.3957 |
| exposure | 0.2050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
