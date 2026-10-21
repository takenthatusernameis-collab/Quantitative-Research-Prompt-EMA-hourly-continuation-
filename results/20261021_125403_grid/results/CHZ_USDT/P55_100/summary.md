# EMA Hourly Continuation — CHZ/USDT P55_100

**Symbol:** CHZ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.0134 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.6065 |
| sortino_ratio | -0.4084 |
| max_drawdown | 0.3892 |
| cagr | -0.1711 |
| net_avg_win | 69.0981 |
| net_avg_loss | -94.0722 |
| avg_hold_time_bars | 8.3885 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
