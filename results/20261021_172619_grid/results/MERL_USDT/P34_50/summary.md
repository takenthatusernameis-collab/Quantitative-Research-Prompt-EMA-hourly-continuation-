# EMA Hourly Continuation — MERL/USDT P34_50

**Symbol:** MERL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7054 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -1.8125 |
| sortino_ratio | -0.4478 |
| max_drawdown | 0.4180 |
| cagr | -0.1858 |
| net_avg_win | 66.9101 |
| net_avg_loss | -88.6947 |
| avg_hold_time_bars | 5.0403 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
