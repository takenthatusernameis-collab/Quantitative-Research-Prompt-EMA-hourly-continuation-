# EMA Hourly Continuation — SHR/USDT P20_26

**Symbol:** SHR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1415 |
| net_profit_factor | 0.2149 |
| net_win_rate | 0.2537 |
| gross_profit_factor | 0.4489 |
| gross_win_rate | 0.2671 |
| sharpe_ratio | -17.9324 |
| sortino_ratio | -9.6935 |
| max_drawdown | 1.0000 |
| cagr | -0.9938 |
| net_avg_win | 7.6243 |
| net_avg_loss | -12.0616 |
| avg_hold_time_bars | 2.2396 |
| exposure | 0.1434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
