# EMA Hourly Continuation — LQTY/USDT P21_34

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7158 |
| net_win_rate | 0.5121 |
| gross_profit_factor | 1.0371 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -2.1782 |
| sortino_ratio | -0.6675 |
| max_drawdown | 0.5384 |
| cagr | -0.2633 |
| net_avg_win | 58.0759 |
| net_avg_loss | -85.1567 |
| avg_hold_time_bars | 5.2571 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
