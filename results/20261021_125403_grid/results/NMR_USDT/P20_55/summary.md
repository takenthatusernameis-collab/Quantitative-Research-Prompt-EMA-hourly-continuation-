# EMA Hourly Continuation — NMR/USDT P20_55

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.7145 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.1103 |
| sortino_ratio | -1.0900 |
| max_drawdown | 0.7302 |
| cagr | -0.3934 |
| net_avg_win | 61.9329 |
| net_avg_loss | -79.7747 |
| avg_hold_time_bars | 8.1542 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
