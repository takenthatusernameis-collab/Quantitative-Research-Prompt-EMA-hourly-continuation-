# EMA Hourly Continuation — PHA/USDT P20_55

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.5103 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8563 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -6.2301 |
| sortino_ratio | -2.7185 |
| max_drawdown | 0.9636 |
| cagr | -0.7309 |
| net_avg_win | 23.1234 |
| net_avg_loss | -37.3871 |
| avg_hold_time_bars | 5.6865 |
| exposure | 0.2481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
