# EMA Hourly Continuation — TNSR/USDT P21_144

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.6424 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8870 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -3.3550 |
| sortino_ratio | -1.0551 |
| max_drawdown | 0.7391 |
| cagr | -0.3973 |
| net_avg_win | 55.5955 |
| net_avg_loss | -73.3272 |
| avg_hold_time_bars | 23.4724 |
| exposure | 0.5396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
