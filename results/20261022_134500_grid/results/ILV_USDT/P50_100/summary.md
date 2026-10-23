# EMA Hourly Continuation — ILV/USDT P50_100

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6108 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -4.2123 |
| sortino_ratio | -1.4580 |
| max_drawdown | 0.8287 |
| cagr | -0.5032 |
| net_avg_win | 45.4091 |
| net_avg_loss | -67.2825 |
| avg_hold_time_bars | 6.5449 |
| exposure | 0.1791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
