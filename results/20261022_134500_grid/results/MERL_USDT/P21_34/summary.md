# EMA Hourly Continuation — MERL/USDT P21_34

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.4234 |
| net_win_rate | 0.4219 |
| gross_profit_factor | 0.7034 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -8.9884 |
| sortino_ratio | -4.2676 |
| max_drawdown | 0.9952 |
| cagr | -0.8809 |
| net_avg_win | 15.1905 |
| net_avg_loss | -26.1884 |
| avg_hold_time_bars | 2.7912 |
| exposure | 0.1450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
