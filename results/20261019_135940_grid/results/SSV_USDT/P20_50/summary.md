# EMA Hourly Continuation — SSV/USDT P20_50

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -7.0974 |
| sortino_ratio | -3.2707 |
| max_drawdown | 0.9809 |
| cagr | -0.7904 |
| net_avg_win | 25.2549 |
| net_avg_loss | -36.6998 |
| avg_hold_time_bars | 4.9944 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
