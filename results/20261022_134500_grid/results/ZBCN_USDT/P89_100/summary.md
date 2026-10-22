# EMA Hourly Continuation — ZBCN/USDT P89_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.2624 |
| net_win_rate | 0.3699 |
| gross_profit_factor | 0.6308 |
| gross_win_rate | 0.3874 |
| sharpe_ratio | -9.8519 |
| sortino_ratio | -3.7402 |
| max_drawdown | 0.9917 |
| cagr | -0.8563 |
| net_avg_win | 13.9465 |
| net_avg_loss | -31.1950 |
| avg_hold_time_bars | 1.8640 |
| exposure | 0.0590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
