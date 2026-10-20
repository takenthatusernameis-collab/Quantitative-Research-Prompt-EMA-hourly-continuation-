# EMA Hourly Continuation — CETUS/USDT P89_100

**Symbol:** CETUS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.4056 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.9329 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -7.5778 |
| sortino_ratio | -2.6162 |
| max_drawdown | 0.9678 |
| cagr | -0.7414 |
| net_avg_win | 25.7784 |
| net_avg_loss | -48.7106 |
| avg_hold_time_bars | 2.2220 |
| exposure | 0.0593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
