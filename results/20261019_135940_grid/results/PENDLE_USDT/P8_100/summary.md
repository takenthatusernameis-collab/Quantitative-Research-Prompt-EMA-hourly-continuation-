# EMA Hourly Continuation — PENDLE/USDT P8_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.6865 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -2.7807 |
| sortino_ratio | -0.9666 |
| max_drawdown | 0.6800 |
| cagr | -0.3647 |
| net_avg_win | 51.1658 |
| net_avg_loss | -69.2940 |
| avg_hold_time_bars | 24.6854 |
| exposure | 0.6777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
