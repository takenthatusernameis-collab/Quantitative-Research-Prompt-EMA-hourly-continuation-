# EMA Hourly Continuation — MTL/USDT P34_89

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.4803 |
| net_win_rate | 0.4250 |
| gross_profit_factor | 0.7869 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -6.1164 |
| sortino_ratio | -2.0991 |
| max_drawdown | 0.9318 |
| cagr | -0.6487 |
| net_avg_win | 33.2600 |
| net_avg_loss | -51.1941 |
| avg_hold_time_bars | 12.0577 |
| exposure | 0.3312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
