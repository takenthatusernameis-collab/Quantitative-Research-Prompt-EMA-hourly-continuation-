# EMA Hourly Continuation — JTO/USDT P34_50

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8658 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -2.4663 |
| sortino_ratio | -0.6287 |
| max_drawdown | 0.5317 |
| cagr | -0.2509 |
| net_avg_win | 63.1837 |
| net_avg_loss | -84.8562 |
| avg_hold_time_bars | 5.6991 |
| exposure | 0.0826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
