# EMA Hourly Continuation — BRETT/USDT P55_144

**Symbol:** BRETT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7907 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9251 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.3358 |
| sortino_ratio | -0.3438 |
| max_drawdown | 0.3447 |
| cagr | -0.1471 |
| net_avg_win | 80.2414 |
| net_avg_loss | -93.8750 |
| avg_hold_time_bars | 16.9481 |
| exposure | 0.2512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
