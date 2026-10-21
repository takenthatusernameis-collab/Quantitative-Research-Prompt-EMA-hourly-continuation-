# EMA Hourly Continuation — PHA/USDT P20_21

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 169 |
| net_profit_factor | 0.9307 |
| net_win_rate | 0.5562 |
| gross_profit_factor | 1.2486 |
| gross_win_rate | 0.5562 |
| sharpe_ratio | -0.2770 |
| sortino_ratio | -0.0523 |
| max_drawdown | 0.2091 |
| cagr | -0.0259 |
| net_avg_win | 90.9762 |
| net_avg_loss | -122.5196 |
| avg_hold_time_bars | 4.5266 |
| exposure | 0.0348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
