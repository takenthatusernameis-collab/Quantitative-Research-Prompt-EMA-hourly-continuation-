# EMA Hourly Continuation — DEGEN/USDT P21_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.0388 |
| sortino_ratio | -1.0903 |
| max_drawdown | 0.7460 |
| cagr | -0.4025 |
| net_avg_win | 63.5097 |
| net_avg_loss | -80.0348 |
| avg_hold_time_bars | 14.5241 |
| exposure | 0.4252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
