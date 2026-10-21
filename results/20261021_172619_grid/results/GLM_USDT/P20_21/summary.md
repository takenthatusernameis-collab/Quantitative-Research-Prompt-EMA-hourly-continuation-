# EMA Hourly Continuation — GLM/USDT P20_21

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.5381 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9168 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -3.7106 |
| sortino_ratio | -0.9310 |
| max_drawdown | 0.6724 |
| cagr | -0.3486 |
| net_avg_win | 54.8465 |
| net_avg_loss | -87.5472 |
| avg_hold_time_bars | 4.8416 |
| exposure | 0.0667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
