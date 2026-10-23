# EMA Hourly Continuation — ALT/USDT P20_34

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.4616 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -7.9590 |
| sortino_ratio | -3.5054 |
| max_drawdown | 0.9868 |
| cagr | -0.8200 |
| net_avg_win | 19.9942 |
| net_avg_loss | -33.4968 |
| avg_hold_time_bars | 4.0969 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
