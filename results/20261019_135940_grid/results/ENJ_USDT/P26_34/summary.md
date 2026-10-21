# EMA Hourly Continuation — ENJ/USDT P26_34

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.2939 |
| net_win_rate | 0.3974 |
| gross_profit_factor | 0.8419 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -12.2581 |
| sortino_ratio | -5.8200 |
| max_drawdown | 0.9995 |
| cagr | -0.9525 |
| net_avg_win | 9.6298 |
| net_avg_loss | -21.6114 |
| avg_hold_time_bars | 2.0396 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
