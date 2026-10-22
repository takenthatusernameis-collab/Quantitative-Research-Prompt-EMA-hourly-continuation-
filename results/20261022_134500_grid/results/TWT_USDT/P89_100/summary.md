# EMA Hourly Continuation — TWT/USDT P89_100

**Symbol:** TWT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.1804 |
| net_win_rate | 0.3282 |
| gross_profit_factor | 0.6942 |
| gross_win_rate | 0.4003 |
| sharpe_ratio | -11.7534 |
| sortino_ratio | -4.5065 |
| max_drawdown | 0.9974 |
| cagr | -0.9059 |
| net_avg_win | 10.2593 |
| net_avg_loss | -27.7832 |
| avg_hold_time_bars | 2.0997 |
| exposure | 0.0622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
