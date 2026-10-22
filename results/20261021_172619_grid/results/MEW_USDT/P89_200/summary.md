# EMA Hourly Continuation — MEW/USDT P89_200

**Symbol:** MEW/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6944 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -1.9617 |
| sortino_ratio | -0.4729 |
| max_drawdown | 0.4447 |
| cagr | -0.1965 |
| net_avg_win | 71.6729 |
| net_avg_loss | -89.2375 |
| avg_hold_time_bars | 17.2768 |
| exposure | 0.2270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
