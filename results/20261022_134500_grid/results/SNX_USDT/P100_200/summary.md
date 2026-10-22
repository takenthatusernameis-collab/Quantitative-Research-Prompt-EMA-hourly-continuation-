# EMA Hourly Continuation — SNX/USDT P100_200

**Symbol:** SNX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6009 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.9462 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -3.4360 |
| sortino_ratio | -0.9509 |
| max_drawdown | 0.6861 |
| cagr | -0.3607 |
| net_avg_win | 58.5352 |
| net_avg_loss | -81.1019 |
| avg_hold_time_bars | 9.5561 |
| exposure | 0.1656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
