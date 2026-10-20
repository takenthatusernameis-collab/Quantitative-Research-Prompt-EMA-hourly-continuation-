# EMA Hourly Continuation — PHA/USDT P89_100

**Symbol:** PHA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.2496 |
| net_win_rate | 0.3841 |
| gross_profit_factor | 0.6298 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -8.7944 |
| sortino_ratio | -3.1693 |
| max_drawdown | 0.9835 |
| cagr | -0.8002 |
| net_avg_win | 13.5014 |
| net_avg_loss | -33.7427 |
| avg_hold_time_bars | 2.2476 |
| exposure | 0.0644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
