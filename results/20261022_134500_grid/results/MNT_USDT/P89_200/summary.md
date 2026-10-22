# EMA Hourly Continuation — MNT/USDT P89_200

**Symbol:** MNT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.4906 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8211 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.3678 |
| sortino_ratio | -0.8485 |
| max_drawdown | 0.6570 |
| cagr | -0.3361 |
| net_avg_win | 41.5405 |
| net_avg_loss | -72.0875 |
| avg_hold_time_bars | 14.6605 |
| exposure | 0.2159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
