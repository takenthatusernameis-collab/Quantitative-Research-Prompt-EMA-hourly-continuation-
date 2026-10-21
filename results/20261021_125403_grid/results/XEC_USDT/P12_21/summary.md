# EMA Hourly Continuation — XEC/USDT P12_21

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.5262 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -4.7722 |
| sortino_ratio | -1.6110 |
| max_drawdown | 0.8518 |
| cagr | -0.5213 |
| net_avg_win | 36.8997 |
| net_avg_loss | -59.5759 |
| avg_hold_time_bars | 4.8915 |
| exposure | 0.1224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
