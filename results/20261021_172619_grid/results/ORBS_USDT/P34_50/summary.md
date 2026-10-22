# EMA Hourly Continuation — ORBS/USDT P34_50

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.4797 |
| net_win_rate | 0.4082 |
| gross_profit_factor | 0.7919 |
| gross_win_rate | 0.4110 |
| sharpe_ratio | -4.9652 |
| sortino_ratio | -1.3613 |
| max_drawdown | 0.8005 |
| cagr | -0.4669 |
| net_avg_win | 49.1391 |
| net_avg_loss | -70.6559 |
| avg_hold_time_bars | 6.5671 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
