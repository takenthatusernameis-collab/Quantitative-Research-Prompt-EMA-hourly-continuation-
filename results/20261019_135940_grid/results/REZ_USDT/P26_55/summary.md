# EMA Hourly Continuation — REZ/USDT P26_55

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 897 |
| net_profit_factor | 0.6173 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 1.0086 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -5.7588 |
| sortino_ratio | -2.4368 |
| max_drawdown | 0.9546 |
| cagr | -0.6957 |
| net_avg_win | 36.9104 |
| net_avg_loss | -51.2510 |
| avg_hold_time_bars | 5.0814 |
| exposure | 0.2103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
