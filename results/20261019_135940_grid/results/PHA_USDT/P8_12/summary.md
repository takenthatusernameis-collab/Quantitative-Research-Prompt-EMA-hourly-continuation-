# EMA Hourly Continuation — PHA/USDT P8_12

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1803 |
| net_profit_factor | 0.2347 |
| net_win_rate | 0.3821 |
| gross_profit_factor | 0.6807 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -15.5736 |
| sortino_ratio | -9.4264 |
| max_drawdown | 1.0000 |
| cagr | -0.9927 |
| net_avg_win | 4.4511 |
| net_avg_loss | -11.7296 |
| avg_hold_time_bars | 1.9179 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
