# EMA Hourly Continuation — LDO/USDT P8_55

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.5593 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8691 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -6.2640 |
| sortino_ratio | -2.7387 |
| max_drawdown | 0.9669 |
| cagr | -0.7419 |
| net_avg_win | 27.6972 |
| net_avg_loss | -40.5480 |
| avg_hold_time_bars | 11.7114 |
| exposure | 0.5238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
