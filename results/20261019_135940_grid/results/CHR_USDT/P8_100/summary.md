# EMA Hourly Continuation — CHR/USDT P8_100

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 1.0043 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -2.5621 |
| sortino_ratio | -0.8824 |
| max_drawdown | 0.6727 |
| cagr | -0.3399 |
| net_avg_win | 59.9886 |
| net_avg_loss | -79.5020 |
| avg_hold_time_bars | 26.0926 |
| exposure | 0.7013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
