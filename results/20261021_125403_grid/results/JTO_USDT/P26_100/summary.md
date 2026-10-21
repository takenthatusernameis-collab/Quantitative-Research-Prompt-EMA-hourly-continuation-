# EMA Hourly Continuation — JTO/USDT P26_100

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7833 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9380 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -1.6893 |
| sortino_ratio | -0.5116 |
| max_drawdown | 0.4988 |
| cagr | -0.2104 |
| net_avg_win | 74.5428 |
| net_avg_loss | -88.2474 |
| avg_hold_time_bars | 16.1840 |
| exposure | 0.3318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
