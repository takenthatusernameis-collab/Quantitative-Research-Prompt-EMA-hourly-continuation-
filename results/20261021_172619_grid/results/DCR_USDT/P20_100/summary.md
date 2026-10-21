# EMA Hourly Continuation — DCR/USDT P20_100

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7024 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9094 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.3141 |
| sortino_ratio | -0.7572 |
| max_drawdown | 0.6207 |
| cagr | -0.2951 |
| net_avg_win | 54.0301 |
| net_avg_loss | -72.1340 |
| avg_hold_time_bars | 16.6030 |
| exposure | 0.3974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
