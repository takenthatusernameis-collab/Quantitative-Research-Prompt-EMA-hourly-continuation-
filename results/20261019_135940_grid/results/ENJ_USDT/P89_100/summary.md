# EMA Hourly Continuation — ENJ/USDT P89_100

**Symbol:** ENJ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.3333 |
| net_win_rate | 0.3937 |
| gross_profit_factor | 0.8560 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -8.8347 |
| sortino_ratio | -3.1386 |
| max_drawdown | 0.9833 |
| cagr | -0.8011 |
| net_avg_win | 20.5607 |
| net_avg_loss | -40.0647 |
| avg_hold_time_bars | 2.4201 |
| exposure | 0.0665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
