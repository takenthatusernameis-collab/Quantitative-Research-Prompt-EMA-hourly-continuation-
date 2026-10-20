# EMA Hourly Continuation — YGG/USDT P50_100

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6589 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 1.0096 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -3.3141 |
| sortino_ratio | -1.1918 |
| max_drawdown | 0.7693 |
| cagr | -0.4278 |
| net_avg_win | 45.1665 |
| net_avg_loss | -68.9804 |
| avg_hold_time_bars | 5.9348 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
