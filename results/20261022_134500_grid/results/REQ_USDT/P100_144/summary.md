# EMA Hourly Continuation — REQ/USDT P100_144

**Symbol:** REQ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.3215 |
| net_win_rate | 0.3399 |
| gross_profit_factor | 0.8160 |
| gross_win_rate | 0.3809 |
| sharpe_ratio | -10.6668 |
| sortino_ratio | -3.9824 |
| max_drawdown | 0.9947 |
| cagr | -0.8744 |
| net_avg_win | 21.0377 |
| net_avg_loss | -33.6962 |
| avg_hold_time_bars | 4.2974 |
| exposure | 0.1287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
