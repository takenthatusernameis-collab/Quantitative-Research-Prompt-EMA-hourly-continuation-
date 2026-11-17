# EMA Hourly Continuation — NUM/USDT P34_100

**Symbol:** NUM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.4585 |
| net_win_rate | 0.3784 |
| gross_profit_factor | 0.6946 |
| gross_win_rate | 0.3844 |
| sharpe_ratio | -6.8343 |
| sortino_ratio | -2.4793 |
| max_drawdown | 0.9519 |
| cagr | -0.6950 |
| net_avg_win | 31.8993 |
| net_avg_loss | -42.3476 |
| avg_hold_time_bars | 10.1306 |
| exposure | 0.3067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
