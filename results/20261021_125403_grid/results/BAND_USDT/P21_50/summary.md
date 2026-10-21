# EMA Hourly Continuation — BAND/USDT P21_50

**Symbol:** BAND/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.7016 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -3.1790 |
| sortino_ratio | -1.1361 |
| max_drawdown | 0.7496 |
| cagr | -0.4059 |
| net_avg_win | 56.5510 |
| net_avg_loss | -75.8603 |
| avg_hold_time_bars | 7.4769 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
