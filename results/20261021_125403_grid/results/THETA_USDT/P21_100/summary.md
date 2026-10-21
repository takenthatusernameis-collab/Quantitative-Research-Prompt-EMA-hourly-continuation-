# EMA Hourly Continuation — THETA/USDT P21_100

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7807 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.6412 |
| sortino_ratio | -0.4907 |
| max_drawdown | 0.4896 |
| cagr | -0.2027 |
| net_avg_win | 72.1779 |
| net_avg_loss | -88.3210 |
| avg_hold_time_bars | 18.1256 |
| exposure | 0.3609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
