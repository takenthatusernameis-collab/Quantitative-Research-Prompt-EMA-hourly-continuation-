# EMA Hourly Continuation — TRAC/USDT P12_100

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.6722 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9612 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -3.5161 |
| sortino_ratio | -1.3132 |
| max_drawdown | 0.7986 |
| cagr | -0.4653 |
| net_avg_win | 47.9433 |
| net_avg_loss | -66.0583 |
| avg_hold_time_bars | 14.7163 |
| exposure | 0.4716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
