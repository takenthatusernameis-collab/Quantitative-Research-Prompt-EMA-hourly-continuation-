# EMA Hourly Continuation — SAND/USDT P26_100

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5355 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8477 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -5.0938 |
| sortino_ratio | -1.8003 |
| max_drawdown | 0.8955 |
| cagr | -0.5821 |
| net_avg_win | 36.1790 |
| net_avg_loss | -54.4753 |
| avg_hold_time_bars | 11.8312 |
| exposure | 0.3410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
