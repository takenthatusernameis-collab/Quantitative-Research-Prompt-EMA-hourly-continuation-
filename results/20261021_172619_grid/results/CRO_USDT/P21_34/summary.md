# EMA Hourly Continuation — CRO/USDT P21_34

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.4898 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.7998 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -3.9324 |
| sortino_ratio | -0.9982 |
| max_drawdown | 0.6928 |
| cagr | -0.3705 |
| net_avg_win | 47.8135 |
| net_avg_loss | -77.4202 |
| avg_hold_time_bars | 5.3526 |
| exposure | 0.0759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
