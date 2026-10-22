# EMA Hourly Continuation — COMP/USDT P8_50

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1127 |
| net_profit_factor | 0.4712 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8109 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -7.0537 |
| sortino_ratio | -3.3288 |
| max_drawdown | 0.9833 |
| cagr | -0.8024 |
| net_avg_win | 16.9439 |
| net_avg_loss | -30.4747 |
| avg_hold_time_bars | 9.4419 |
| exposure | 0.4837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
