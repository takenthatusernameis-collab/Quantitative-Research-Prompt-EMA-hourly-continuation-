# EMA Hourly Continuation — CHZ/USDT P26_100

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.8202 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0402 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.2514 |
| sortino_ratio | -0.3704 |
| max_drawdown | 0.3940 |
| cagr | -0.1579 |
| net_avg_win | 73.6991 |
| net_avg_loss | -93.7441 |
| avg_hold_time_bars | 17.4682 |
| exposure | 0.3375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
