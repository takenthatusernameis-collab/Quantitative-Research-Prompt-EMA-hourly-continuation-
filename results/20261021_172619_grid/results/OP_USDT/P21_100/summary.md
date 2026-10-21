# EMA Hourly Continuation — OP/USDT P21_100

**Symbol:** OP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.5825 |
| sortino_ratio | -0.4580 |
| max_drawdown | 0.4615 |
| cagr | -0.1907 |
| net_avg_win | 77.1151 |
| net_avg_loss | -94.2524 |
| avg_hold_time_bars | 23.0243 |
| exposure | 0.4301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
