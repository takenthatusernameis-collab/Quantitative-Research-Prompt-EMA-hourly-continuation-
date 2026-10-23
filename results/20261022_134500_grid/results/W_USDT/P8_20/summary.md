# EMA Hourly Continuation — W/USDT P8_20

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1673 |
| net_profit_factor | 0.4916 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -10.0569 |
| sortino_ratio | -5.8047 |
| max_drawdown | 0.9993 |
| cagr | -0.9428 |
| net_avg_win | 12.8494 |
| net_avg_loss | -21.3412 |
| avg_hold_time_bars | 2.7908 |
| exposure | 0.2122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
