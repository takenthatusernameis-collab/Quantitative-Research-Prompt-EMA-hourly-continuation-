# EMA Hourly Continuation — SUI/USDT P8_21

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8560 |
| net_win_rate | 0.5358 |
| gross_profit_factor | 1.1388 |
| gross_win_rate | 0.5358 |
| sharpe_ratio | -0.9970 |
| sortino_ratio | -0.3096 |
| max_drawdown | 0.3806 |
| cagr | -0.1345 |
| net_avg_win | 73.2320 |
| net_avg_loss | -98.7417 |
| avg_hold_time_bars | 5.5380 |
| exposure | 0.1160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
