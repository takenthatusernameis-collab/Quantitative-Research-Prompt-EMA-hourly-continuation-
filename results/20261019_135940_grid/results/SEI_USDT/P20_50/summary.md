# EMA Hourly Continuation — SEI/USDT P20_50

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.5811 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -6.1585 |
| sortino_ratio | -2.6751 |
| max_drawdown | 0.9627 |
| cagr | -0.7243 |
| net_avg_win | 29.9471 |
| net_avg_loss | -45.5926 |
| avg_hold_time_bars | 5.3186 |
| exposure | 0.2292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
