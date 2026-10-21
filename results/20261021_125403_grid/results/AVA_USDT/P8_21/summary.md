# EMA Hourly Continuation — AVA/USDT P8_21

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.6911 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -2.6133 |
| sortino_ratio | -0.9137 |
| max_drawdown | 0.6837 |
| cagr | -0.3405 |
| net_avg_win | 48.5140 |
| net_avg_loss | -72.1302 |
| avg_hold_time_bars | 5.1576 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
