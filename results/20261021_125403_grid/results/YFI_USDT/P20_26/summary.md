# EMA Hourly Continuation — YFI/USDT P20_26

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.4380 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.8066 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -4.6576 |
| sortino_ratio | -1.2222 |
| max_drawdown | 0.7645 |
| cagr | -0.4328 |
| net_avg_win | 41.1718 |
| net_avg_loss | -73.1726 |
| avg_hold_time_bars | 4.5410 |
| exposure | 0.0676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
