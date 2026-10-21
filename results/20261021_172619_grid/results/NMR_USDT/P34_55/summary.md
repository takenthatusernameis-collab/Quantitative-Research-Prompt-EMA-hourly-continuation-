# EMA Hourly Continuation — NMR/USDT P34_55

**Symbol:** NMR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.6034 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8700 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -3.6066 |
| sortino_ratio | -1.0212 |
| max_drawdown | 0.7120 |
| cagr | -0.3736 |
| net_avg_win | 59.4104 |
| net_avg_loss | -80.6760 |
| avg_hold_time_bars | 5.4453 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
