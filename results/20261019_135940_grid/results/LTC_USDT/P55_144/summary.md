# EMA Hourly Continuation — LTC/USDT P55_144

**Symbol:** LTC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.3593 |
| net_win_rate | 0.4170 |
| gross_profit_factor | 0.7534 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -6.4915 |
| sortino_ratio | -2.1582 |
| max_drawdown | 0.9343 |
| cagr | -0.6569 |
| net_avg_win | 22.6209 |
| net_avg_loss | -45.0277 |
| avg_hold_time_bars | 10.0253 |
| exposure | 0.2525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
