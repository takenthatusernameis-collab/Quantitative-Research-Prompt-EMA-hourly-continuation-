# EMA Hourly Continuation — VET/USDT P26_200

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7933 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9750 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.3160 |
| sortino_ratio | -0.3323 |
| max_drawdown | 0.3531 |
| cagr | -0.1430 |
| net_avg_win | 79.5593 |
| net_avg_loss | -98.3799 |
| avg_hold_time_bars | 39.5208 |
| exposure | 0.5623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
