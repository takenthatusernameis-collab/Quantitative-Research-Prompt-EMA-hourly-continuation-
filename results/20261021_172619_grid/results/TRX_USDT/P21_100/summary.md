# EMA Hourly Continuation — TRX/USDT P21_100

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.5106 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9717 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -4.1959 |
| sortino_ratio | -1.2285 |
| max_drawdown | 0.7643 |
| cagr | -0.4319 |
| net_avg_win | 39.3542 |
| net_avg_loss | -73.7773 |
| avg_hold_time_bars | 19.8029 |
| exposure | 0.3700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
