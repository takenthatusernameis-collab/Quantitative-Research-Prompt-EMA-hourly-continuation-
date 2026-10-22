# EMA Hourly Continuation — BIGTIME/USDT P20_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.8613 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0443 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -0.9114 |
| sortino_ratio | -0.2594 |
| max_drawdown | 0.2900 |
| cagr | -0.1148 |
| net_avg_win | 81.4022 |
| net_avg_loss | -98.9162 |
| avg_hold_time_bars | 30.8937 |
| exposure | 0.5522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
