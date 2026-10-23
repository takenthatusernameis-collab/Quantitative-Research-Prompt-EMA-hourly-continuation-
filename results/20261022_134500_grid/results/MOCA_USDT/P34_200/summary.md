# EMA Hourly Continuation — MOCA/USDT P34_200

**Symbol:** MOCA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.5504 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.7752 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -3.5623 |
| sortino_ratio | -0.9771 |
| max_drawdown | 0.6645 |
| cagr | -0.3775 |
| net_avg_win | 51.8098 |
| net_avg_loss | -76.4819 |
| avg_hold_time_bars | 29.9828 |
| exposure | 0.5231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
