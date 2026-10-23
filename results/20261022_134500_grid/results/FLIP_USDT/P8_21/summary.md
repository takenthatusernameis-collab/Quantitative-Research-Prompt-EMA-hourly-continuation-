# EMA Hourly Continuation — FLIP/USDT P8_21

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1138 |
| net_profit_factor | 0.3299 |
| net_win_rate | 0.3673 |
| gross_profit_factor | 0.7729 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -12.4736 |
| sortino_ratio | -6.0147 |
| max_drawdown | 0.9996 |
| cagr | -0.9568 |
| net_avg_win | 11.7756 |
| net_avg_loss | -20.7201 |
| avg_hold_time_bars | 5.9455 |
| exposure | 0.3075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
