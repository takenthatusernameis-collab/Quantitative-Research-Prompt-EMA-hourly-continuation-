# EMA Hourly Continuation — HTX/USDT P20_100

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.3347 |
| net_win_rate | 0.3402 |
| gross_profit_factor | 0.8133 |
| gross_win_rate | 0.4044 |
| sharpe_ratio | -10.8245 |
| sortino_ratio | -4.2133 |
| max_drawdown | 0.9966 |
| cagr | -0.8946 |
| net_avg_win | 20.1385 |
| net_avg_loss | -31.0150 |
| avg_hold_time_bars | 14.3907 |
| exposure | 0.4767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
