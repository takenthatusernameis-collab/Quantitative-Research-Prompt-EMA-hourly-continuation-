# EMA Hourly Continuation — MERL/USDT P21_100

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8808 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -3.6193 |
| sortino_ratio | -1.3075 |
| max_drawdown | 0.8149 |
| cagr | -0.4619 |
| net_avg_win | 50.6188 |
| net_avg_loss | -65.0802 |
| avg_hold_time_bars | 13.9848 |
| exposure | 0.4194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
