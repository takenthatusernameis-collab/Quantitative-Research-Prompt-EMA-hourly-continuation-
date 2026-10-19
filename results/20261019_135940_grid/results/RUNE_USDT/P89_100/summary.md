# EMA Hourly Continuation — RUNE/USDT P89_100

**Symbol:** RUNE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.2813 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.7046 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -8.7004 |
| sortino_ratio | -2.9585 |
| max_drawdown | 0.9797 |
| cagr | -0.7854 |
| net_avg_win | 17.9102 |
| net_avg_loss | -40.9101 |
| avg_hold_time_bars | 2.1590 |
| exposure | 0.0537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
