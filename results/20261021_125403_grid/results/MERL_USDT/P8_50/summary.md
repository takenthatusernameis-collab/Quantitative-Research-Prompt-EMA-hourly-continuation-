# EMA Hourly Continuation — MERL/USDT P8_50

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.8628 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0191 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -1.1555 |
| sortino_ratio | -0.4401 |
| max_drawdown | 0.4893 |
| cagr | -0.1882 |
| net_avg_win | 71.6493 |
| net_avg_loss | -85.6841 |
| avg_hold_time_bars | 13.8450 |
| exposure | 0.4436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
