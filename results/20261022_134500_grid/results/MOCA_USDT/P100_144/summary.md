# EMA Hourly Continuation — MOCA/USDT P100_144

**Symbol:** MOCA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.4435 |
| net_win_rate | 0.4098 |
| gross_profit_factor | 0.8092 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -6.1597 |
| sortino_ratio | -1.8568 |
| max_drawdown | 0.8819 |
| cagr | -0.6069 |
| net_avg_win | 41.7762 |
| net_avg_loss | -65.3938 |
| avg_hold_time_bars | 4.7244 |
| exposure | 0.0971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
