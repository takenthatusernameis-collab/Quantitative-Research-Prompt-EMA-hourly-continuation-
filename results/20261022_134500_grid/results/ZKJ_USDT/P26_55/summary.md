# EMA Hourly Continuation — ZKJ/USDT P26_55

**Symbol:** ZKJ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.1478 |
| net_win_rate | 0.2724 |
| gross_profit_factor | 0.4371 |
| gross_win_rate | 0.3571 |
| sharpe_ratio | -15.7445 |
| sortino_ratio | -7.5219 |
| max_drawdown | 1.0000 |
| cagr | -0.9837 |
| net_avg_win | 6.0627 |
| net_avg_loss | -15.3581 |
| avg_hold_time_bars | 7.1733 |
| exposure | 0.3424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
