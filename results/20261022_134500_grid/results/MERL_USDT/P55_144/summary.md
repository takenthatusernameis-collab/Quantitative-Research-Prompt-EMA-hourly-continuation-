# EMA Hourly Continuation — MERL/USDT P55_144

**Symbol:** MERL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8583 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -3.5006 |
| sortino_ratio | -1.0944 |
| max_drawdown | 0.7531 |
| cagr | -0.4014 |
| net_avg_win | 56.1972 |
| net_avg_loss | -72.3746 |
| avg_hold_time_bars | 10.7894 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
