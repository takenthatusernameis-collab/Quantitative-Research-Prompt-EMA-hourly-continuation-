# EMA Hourly Continuation — MERL/USDT P26_50

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.4527 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.6978 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -6.9306 |
| sortino_ratio | -2.9848 |
| max_drawdown | 0.9746 |
| cagr | -0.7652 |
| net_avg_win | 19.9838 |
| net_avg_loss | -33.4992 |
| avg_hold_time_bars | 4.2591 |
| exposure | 0.1813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
