# EMA Hourly Continuation — ASTR/USDT P20_100

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.6676 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 1.0181 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -3.1993 |
| sortino_ratio | -1.1150 |
| max_drawdown | 0.7550 |
| cagr | -0.4085 |
| net_avg_win | 49.3068 |
| net_avg_loss | -71.4659 |
| avg_hold_time_bars | 16.3717 |
| exposure | 0.4504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
