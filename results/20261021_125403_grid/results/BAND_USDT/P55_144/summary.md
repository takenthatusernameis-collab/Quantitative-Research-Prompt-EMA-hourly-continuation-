# EMA Hourly Continuation — BAND/USDT P55_144

**Symbol:** BAND/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7617 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -3.1962 |
| sortino_ratio | -0.8631 |
| max_drawdown | 0.6381 |
| cagr | -0.3293 |
| net_avg_win | 55.1101 |
| net_avg_loss | -73.7153 |
| avg_hold_time_bars | 15.1374 |
| exposure | 0.2493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
