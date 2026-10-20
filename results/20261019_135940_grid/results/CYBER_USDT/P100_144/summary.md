# EMA Hourly Continuation — CYBER/USDT P100_144

**Symbol:** CYBER/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.5142 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9436 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.9516 |
| sortino_ratio | -1.1848 |
| max_drawdown | 0.7750 |
| cagr | -0.4398 |
| net_avg_win | 37.0530 |
| net_avg_loss | -67.1544 |
| avg_hold_time_bars | 5.1586 |
| exposure | 0.1065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
