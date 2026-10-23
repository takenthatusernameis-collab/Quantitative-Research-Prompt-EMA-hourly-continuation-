# EMA Hourly Continuation — MOCA/USDT P8_100

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.5681 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8637 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -4.3041 |
| sortino_ratio | -1.4473 |
| max_drawdown | 0.8153 |
| cagr | -0.5075 |
| net_avg_win | 44.2421 |
| net_avg_loss | -64.1380 |
| avg_hold_time_bars | 25.9620 |
| exposure | 0.6859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
