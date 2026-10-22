# EMA Hourly Continuation — RAY/USDT P89_100

**Symbol:** RAY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.2529 |
| net_win_rate | 0.3754 |
| gross_profit_factor | 0.6310 |
| gross_win_rate | 0.4185 |
| sharpe_ratio | -9.1933 |
| sortino_ratio | -3.3106 |
| max_drawdown | 0.9869 |
| cagr | -0.8199 |
| net_avg_win | 14.2134 |
| net_avg_loss | -33.7728 |
| avg_hold_time_bars | 2.3227 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
