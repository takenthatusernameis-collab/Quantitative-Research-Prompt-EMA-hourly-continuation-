# EMA Hourly Continuation — PHA/USDT P89_200

**Symbol:** PHA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8903 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -2.9635 |
| sortino_ratio | -0.8772 |
| max_drawdown | 0.6565 |
| cagr | -0.3348 |
| net_avg_win | 49.1957 |
| net_avg_loss | -71.8046 |
| avg_hold_time_bars | 9.3210 |
| exposure | 0.1835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
